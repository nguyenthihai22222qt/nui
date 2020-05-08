import tkinter
from inspect import getfullargspec
from typing import Callable


class FlatButton(tkinter.Label):
	def __init__(self, master, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)
		self.bind('<Button-1>', command if getfullargspec(command).args else lambda _: command())

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'FlatButton':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self
