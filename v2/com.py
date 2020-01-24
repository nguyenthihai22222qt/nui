from typing import List, Union

from v2.consts import RetCode


class Com:
	def __init__(self, name: Union[str, List[str]], method: callable, man: str = ''):
		self.name: List[str] = name if isinstance(name, List) else name.strip().split(' ')
		self.method: callable = method
		self.man = man  # TODO Better help

	def run(self, rt):
		if rt.args[1] in ['help']:
			return rt.quick(RetCode.HELP, self.man)
		else:
			return self.method(rt)
