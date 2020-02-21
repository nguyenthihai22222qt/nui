import tkinter
from inspect import getfullargspec
from typing import Callable

from .. import Style


class FlatButton(tkinter.Label):
	def __init__(self, master, style: Style, command: Callable, **kw):
		super().__init__(master, bg=style.bg, fg=style.fg, **kw)
		self.style = style
		self.bind('<Button-1>', command if getfullargspec(command).args else lambda _: command())
