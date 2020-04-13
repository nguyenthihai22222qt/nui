import tkinter
from typing import Callable

from .ipack import IPack


class Label(tkinter.Label, IPack):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)


class Button(tkinter.Button, IPack):
	def __init__(self, master, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, command=command, **kw)


class Entry(tkinter.Entry, IPack):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)


class Text(tkinter.Text, IPack):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)
