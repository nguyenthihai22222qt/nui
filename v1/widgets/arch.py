import tkinter
from typing import Callable

from .basic import Label


class Frame(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def inline_add(self, widget, widget_kw=None, pack_kw=None) -> 'Frame':
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, **widget_kw).pack(**pack_kw)
		return self

	def add(self, widget, widget_kw=None, pack_kw=None):
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		w = widget(self, **widget_kw)
		w.pack(**pack_kw)
		return w


class Field(Frame):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, **kw)
		self.label = Label(self, text=label)
		self.label.pack(side='left')
		self.b_get = lambda: None
		self.auto_write: Callable[[], None] = lambda: None

	def read(self):
		self.set_(self.b_get())

	def get(self):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR

	def set_(self, value):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR
