from .com import Com
from .consts import RetCode
from .retcom import RetCom
from .shell import Shell


# noinspection PyMethodMayBeStatic
class Api:
	__default = None

	def __init__(self):
		self.commands = []
		self.shell: Shell = Shell(self)
		self.rc: RetCom = RetCom(None, None, [], '')

	def parse_args(self, arg: str) -> str:
		# Overwrite me
		return arg

	# fun = com()(fun) NOSONAR
	@staticmethod
	def com(com: Com, api: 'Api' = None):
		def decorator(fun):
			# fun.api = api #NOSONAR Could be used
			com.method = com.method if com.method else fun
			return fun

		api = api if api else Api.get_default()
		api.commands.append(com)
		return decorator

	@staticmethod
	def get_default():
		Api.__default = Api.__default if Api.__default else Api()
		return Api.__default

	def quick_run(self, com: str):
		rc: RetCom
		for rc in self.shell.line_com_parser(com):
			if rc.code == RetCode.EXIT:
				return False
			elif rc.code == RetCode.EMPTY:
				continue
			elif rc.code == RetCode.ERROR:
				print(f"[Error] {rc.com.name}{(': ' + rc.answer) if rc.answer else ''}")
			elif rc.code == RetCode.PATH_ERROR:
				print(f"[Path Error] {rc.com.name}: {rc.answer}")
			elif rc.code == RetCode.ARGS_ERROR:
				print(f"[Args Error] {rc.com.name}{(': ' + rc.answer) if rc.answer else ''}")
			elif rc.code == RetCode.UNKNOWN:
				print(f"[Unknown command] {rc.com.name}")
			elif rc.answer:
				print(rc.answer)
		return True

	def quick_run_loop(self, add_to_path: str = '>'):
		while self.quick_run(input(f'{self.shell.path}{add_to_path}')):
			pass  # NOSONAR
