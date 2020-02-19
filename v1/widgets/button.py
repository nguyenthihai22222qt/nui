from tkinter import Button as tkButton
from typing import Callable

from ..style import Style


class Button(tkButton):
	def __init__(self, master, style: 'Style', command: Callable, **kw):
		super().__init__(master, bg=style.bg, fg=style.fg, command=command, **kw)
		self.style = style
