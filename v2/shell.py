from typing import Iterator, List

from v2.com import Com
from v2.retcom import RetCom


class Shell:
	def __init__(self, commands: List[Com]):
		self.commands: List[Com] = commands
		self.unknown = Com([], lambda rc: rc.unknown(), '')

	def _get_com(self, c: str) -> Com:  # TODO Wrapper around Coms
		for com in self.commands:
			if c in com.name:
				return com
		return self.unknown

	def line_com_parser(self, c: str) -> Iterator[RetCom]:
		for co in c.split('|'):
			co = self._com_parse(co)
			c = co[0]
			args = co[1:]
			com = self._get_com(c)
			yield com.method(RetCom(self, com, args))

	@staticmethod
	def _com_parse(c: str) -> list:
		o = []
		tmp = ''
		in_string = False
		for co in c:
			if co == ' ' and not in_string:
				if tmp:
					o.append(tmp)
				tmp = ''
			elif co not in ["'", '"']:
				tmp += co
			else:
				if not in_string:
					tmp = ''
				in_string = not in_string
		if tmp:
			o.append(tmp)
		elif not o:
			o.append('')
		return o
