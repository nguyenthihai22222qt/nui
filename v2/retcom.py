from typing import List

from .consts import RetCode


class RetCom:
	def __init__(self, shell, com, args: List[str]):
		self.shell = shell
		self.com = com
		self.args: List[str] = args
		self.code: RetCode = RetCode.NONE
		self.answer: str = ''

	def answer(self, code: RetCode = RetCode.OK, answer: str = '') -> 'RetCom':
		self.answer = answer
		self.code = code
		return self

	def unknown(self, answer: str = '') -> 'RetCom':
		self.answer = answer
		self.code = RetCode.UNKNOWN
		return self

	def error(self, answer: str = '') -> 'RetCom':
		self.answer = answer
		self.code = RetCode.ERROR
		return self
