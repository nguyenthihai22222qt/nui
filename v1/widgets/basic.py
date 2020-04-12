import tkinter
from typing import Callable


class Label(tkinter.Label):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, **kw)

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Label':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self


class Button(tkinter.Button):
	def __init__(self, master, command: Callable, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, command=command, **kw)

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Button':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self


class Entry(tkinter.Entry):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Entry':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self


class Text(tkinter.Text):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, fg=self.stage.style.fg, insertbackground=self.stage.style.fg, **kw)

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Text':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self
