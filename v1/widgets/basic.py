import tkinter
from typing import Callable


class Label(tkinter.Label):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)


class Button(tkinter.Button):
	def __init__(self, master, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, command=command, **kw)


class Entry(tkinter.Entry):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)


class Text(tkinter.Text):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)
