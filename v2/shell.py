from typing import Iterator

from v2.api import Api
from v2.com import Com
from v2.retcom import RetCom


class Shell:
	def __init__(self, api: Api):
		self.api: Api = api
		self.unknown = Com([], lambda rc: rc.unknown(), '')

	def _get_com(self, c: str) -> Com:  # TODO Wrapper around Commands
		for com in self.api.get_commands():
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
					o.append(tmp)  # TODO Parse though api
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
