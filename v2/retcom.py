from typing import List

from v2.consts import RetCode


class RetCom:
	def __init__(self, shell, com, args: List[str]):
		self.shell = shell
		self.com = com
		self.args: List[str] = args
		self.code: RetCode = RetCode.NONE
		self.answer: str = ''

	def unknown(self):
		self.code = RetCode.UNKNOWN
		return self
