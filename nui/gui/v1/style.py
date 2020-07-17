from typing import Tuple


class Style:
	def __init__(self, /, *, bg: str = 'white', fg: str = 'black', font: Tuple[str, int] = None):
		self.bg = bg
		self.fg = fg
		self.font = font
