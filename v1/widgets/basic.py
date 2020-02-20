import tkinter
from typing import Callable

from ..style import Style


class Label(tkinter.Label):
	def __init__(self, master, style: 'Style', **kw):
		super().__init__(master, bg=style.bg, fg=style.fg, **kw)
		self.style = style


class Button(tkinter.Button):
	def __init__(self, master, style: 'Style', command: Callable, **kw):
		super().__init__(master, bg=style.bg, fg=style.fg, command=command, **kw)
		self.style = style
