import tkinter

from v1.style import Style


class Label(tkinter.Label):
	def __init__(self, master, style: Style, **kw):
		super().__init__(master, **kw, fg=style.fg, bg=style.bg)
		self.style = style
