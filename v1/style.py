class Style:
	def __init__(self, bg: str = 'white', fg: str = 'black'):
		self.bg = bg
		self.fg = fg

	def quick(self, bg=False, fg=False):
		o = {}
		if bg:
			o['bg'] = self.bg
		if fg:
			o['fg'] = self.fg
		return o
