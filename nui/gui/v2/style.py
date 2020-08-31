class Style:
	def __init__(self, /, *, bg: str = 'white', fg: str = 'black', font_family: str = None, font_size: int = 10):
		self.bg = bg if bg else None
		self.fg = fg if fg else None
		self.font_family = font_family if font_family else None
		self.font_size = font_size if font_size else None

	def child(self, bg: str = None, fg: str = None, font_family: str = None, font_size: int = 10):
		return Style(
			bg=bg if bg else self.bg,
			fg=fg if fg else self.fg,
			font_family=font_family if font_family else self.font_family,
			font_size=font_size if font_size else self.font_size
		)

	@property
	def font(self):
		return self.font_family, self.font_size

	@staticmethod
	def from_dict(in_: dict) -> 'Style':
		return Style(**in_)

	def to_dict(self) -> dict:
		return {
			'fg': self.fg,
			'bg': self.bg,
			'font_family': self.font_family,
			'font_size': self.font_size
		}
