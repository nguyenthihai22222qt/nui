from typing import List, Union

from v2.consts import RetCode


class Com:
	def __init__(self, name: Union[str, List[str]], method: callable, man: str = ''):
		self.name: List[str] = name if isinstance(name, List) else name.strip().split(' ')  # FIXME Spaces in list elements
		self.method: callable = method
		self.man = man  # TODO Better help

	def run(self, rt):
		if len(rt.args) > 1 and rt.args[1] in ['help']:
			return rt.quick(self.man, RetCode.HELP)
		else:
			return self.method(rt)
