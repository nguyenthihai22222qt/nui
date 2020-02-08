from typing import List, Union

from .consts import RetCode


class Com:
	def __init__(self, name: Union[str, List[str]], method: callable, man: str = ''):
		self.name: List[str] = name if isinstance(name, List) else name.strip().split(' ')  # FIXME Spaces in list elements
		self.method: callable = method
		self.man = man  # TODO Better help

	def run(self, api, ret_com):
		api.rc = ret_com
		if len(api.rc.args) > 1 and api.rc.args[1] in ['help']:
			return api.rc.quick(self.man, RetCode.HELP)
		else:
			o = self.method()
			return o if o else api.rc
