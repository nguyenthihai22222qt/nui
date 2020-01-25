from typing import List

from .com import Com
from .consts import RetCode


class RetCom:
	def __init__(self, shell, com, args: List[str]):
		self.shell = shell
		self.com: Com = com
		self.args: List[str] = args
		self.code: RetCode = RetCode.NONE
		self.answer: str = ''

	def quick(self, answer: str = '', code: RetCode = RetCode.OK) -> 'RetCom':
		self.answer = answer
		self.code = code
		return self

	def unknown(self) -> 'RetCom':
		self.answer = self.args[0] if len(self.args) else ''
		self.code = RetCode.UNKNOWN
		return self

	def error(self, answer: str = '') -> 'RetCom':
		self.answer = answer
		self.code = RetCode.ERROR
		return self

	def empty(self):
		self.code = RetCode.EMPTY
		return self
