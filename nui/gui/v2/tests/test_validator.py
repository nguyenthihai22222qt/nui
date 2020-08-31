from unittest import TestCase

from nui.gui.v2 import validator


class TestString(TestCase):
	def test_empty(self):
		self.assertTrue(validator.string()('Hi'))
		self.assertTrue(validator.string()(''))

	def test_allow_char(self):
		self.assertTrue(validator.string(allow_chars='asdASD')(''))
		self.assertTrue(validator.string(allow_chars='asdASD')('adsasdasdaAdsaAS'))
		self.assertFalse(validator.string(allow_chars='asdASD')('adsasdwasdaAdsaAS'))

	def test_block_char(self):
		self.assertTrue(validator.string(block_chars='asdASD')(''))
		self.assertTrue(validator.string(block_chars='asdASD')('qweqwrqwrqweqweqrqw'))
		self.assertFalse(validator.string(block_chars='asdASD')('qweqweqweqAeweqew'))

	def test_allow_empty(self):
		self.assertTrue(validator.string(allow_empty=False)('Hi'))
		self.assertFalse(validator.string(allow_empty=False)(''))

	def test_max_length(self):
		self.assertTrue(validator.string(max_length=3)(''))
		self.assertTrue(validator.string(max_length=3)('Hi'))
		self.assertTrue(validator.string(max_length=3)('Hia'))
		self.assertFalse(validator.string(max_length=3)('Hell'))
		self.assertFalse(validator.string(max_length=3)('Hello'))
		self.assertFalse(validator.string(allow_empty=False, max_length=3)(''))
		self.assertTrue(validator.string(allow_empty=False, max_length=3)('s'))


class TestInteger(TestCase):
	def test_empty(self):
		self.assertTrue(validator.integer()('1'))
		self.assertTrue(validator.integer()('0'))
		self.assertTrue(validator.integer()(''))
		self.assertFalse(validator.integer()('a'))

	def test_min_value(self):
		self.assertTrue(validator.integer(min_value=4)(''))
		self.assertTrue(validator.integer(min_value=4)('5'))
		self.assertTrue(validator.integer(min_value=4)('4'))
		self.assertFalse(validator.integer(min_value=4)('3'))
		self.assertFalse(validator.integer(min_value=4)('2'))
		self.assertFalse(validator.integer(min_value=4)('0'))
		self.assertTrue(validator.integer(min_value=-4)('0'))
		self.assertTrue(validator.integer(min_value=-4)('-1'))
		self.assertFalse(validator.integer(empty=False, min_value=4)(''))

	def test_max_value(self):
		self.assertTrue(validator.integer(max_value=4)(''))
		self.assertFalse(validator.integer(max_value=4)('5'))
		self.assertTrue(validator.integer(max_value=4)('4'))
		self.assertTrue(validator.integer(max_value=4)('3'))
		self.assertTrue(validator.integer(max_value=4)('0'))
		self.assertFalse(validator.integer(max_value=-4)('0'))
		self.assertFalse(validator.integer(max_value=-4)('-1'))
		self.assertFalse(validator.integer(empty=False, max_value=4)(''))

	def test_random(self):
		self.assertTrue(validator.integer(empty=False, max_value=4)('0'))
