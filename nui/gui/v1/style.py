from copy import deepcopy
from typing import Tuple


class Style:
	def __init__(self, /, *, bg: str = 'white', fg: str = 'black', font: Tuple[str, int] = None):
		self.bg = bg if bg else None
		self.fg = fg if fg else None
		self.font = font if font else None

	def child(self, bg: str = None, fg: str = None, font: Tuple[str, int] = None):
		return Style(
			bg=bg if bg else self.bg,
			fg=fg if fg else self.fg,
			font=font if font else deepcopy(self.font)
		)

	@staticmethod
	def from_dict(in_: dict) -> 'Style':
		return Style(bg=in_.get('bg'), fg=in_.get('fg'), font=in_.get('font'))

	def to_dict(self) -> dict:
		return {
			'fg': self.fg,
			'bg': self.bg,
			'font': self.font
		}
