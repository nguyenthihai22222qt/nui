import tkinter
from typing import Callable

from .imethods import IMethods


class Label(tkinter.Label, IMethods):
	def __init__(self, master, text: str = '', **kw):
		self.stage = master.stage
		super().__init__(master, text=text, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)

	def get_(self):
		return self['text']

	def set_(self, value):
		self['text'] = value


class Button(tkinter.Button, IMethods):
	def __init__(self, master, text: str, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, text=text, bg=self.stage.style.bg, fg=self.stage.style.fg, command=command, **kw)

	def get_(self):
		return self['text']

	def set_(self, value) -> None:
		self['text'] = value


class Entry(tkinter.Entry, IMethods):
	def __init__(self, master, width: int = 1, **kw):
		self.stage = master.stage
		super().__init__(master, width=width, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)

	def get_(self):
		return self.get()

	def set_(self, value):
		self.delete(0, 'end')
		self.insert('end', value)


class Text(tkinter.Text, IMethods):
	def __init__(self, master, width: int = 1, height: int = 1, **kw):
		self.stage = master.stage
		super().__init__(master, width=width, height=height, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)

	def get_(self):
		return self.get(1.0, 'end').strip()

	def set_(self, value):
		self.delete(1.0, 'end')
		self.insert('end', value)
