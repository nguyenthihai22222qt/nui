from tkinter import Label as tkLabel

from ..style import Style


class Label(tkLabel):
	def __init__(self, master, style: 'Style', **kw):
		super().__init__(master, bg=style.bg, fg=style.fg, **kw)
		self.style = style
