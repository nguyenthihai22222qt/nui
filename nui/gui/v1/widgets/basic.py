import tkinter
from typing import Callable

from .imethods import IMethods


class Label(tkinter.Label, IMethods):
	def __init__(self, master, text: str = '', **kw):
		self.stage = master.stage
		super().__init__(master, text=text, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)


class Button(tkinter.Button, IMethods):
	def __init__(self, master, text: str, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, text=text, bg=self.stage.style.bg, fg=self.stage.style.fg, command=command, **kw)


class Entry(tkinter.Entry, IMethods):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)


class Text(tkinter.Text, IMethods):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)
