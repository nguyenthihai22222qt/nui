from typing import List
from unittest import TestCase

from .api import Api
from .com import Com
from .consts import RetCode
from .shell import Shell


# Com
class TestCom(TestCase):
	def test_init(self):
		self.assertListEqual(Com('q', None).name, ['q'])
		self.assertListEqual(Com(['wasd'], None).name, ['wasd'])
		self.assertListEqual(Com(['wasd', 'q', 'ewq'], None).name, ['wasd', 'q', 'ewq'])
		self.assertListEqual(Com('wasd q ewq w', None).name, ['wasd', 'q', 'ewq', 'w'])


class Wrap(Api):
	def get_commands(self) -> List[Com]:
		return [
			Com('ok', lambda rt: rt.quick('okay'), 'Doc'),
			Com('er', lambda rt: rt.error('Oops'))
		]

	def parse_args(self, arg: str) -> str:
		return super().parse_args(arg)


# Api/Shell
class TestApiShell(TestCase):
	def _com(self, com: str, code: RetCode, answer: str):
		w = Wrap()
		s = Shell(w)
		w.shell = s
		o = [x for x in s.line_com_parser(com)]
		self.assertEqual(len(o), len(com.split('|')))
		o = o[0]
		self.assertEqual(len(o.args), len(com.split(' ')))
		self.assertIs(o.code, code)
		self.assertEqual(o.answer, answer)

	def test_api_ok(self):
		self._com('ok', RetCode.OK, 'okay')

	def test_api_er(self):
		self._com('er', RetCode.ERROR, 'Oops')

	def test_api_unknown(self):
		self._com('unknown', RetCode.UNKNOWN, 'unknown')

	def test_api_unknown_arg(self):
		self._com('unknown arg', RetCode.UNKNOWN, 'unknown')

	def test_api_ok_help(self):
		self._com('ok help', RetCode.HELP, 'Doc')

	def test_api_empty(self):
		self._com('', RetCode.EMPTY, '')
