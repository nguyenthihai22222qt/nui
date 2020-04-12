import tkinter
from typing import Callable

from .basic import Label


class Frame(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def inline_add(self, widget, widget_kw=None, pack_kw=None) -> 'Frame':
		widget_kw = widget_kw if widget_kw else {}
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, **widget_kw).pack(**pack_kw)
		return self

	def add(self, widget, widget_kw=None, pack_kw=None):
		widget_kw = widget_kw if widget_kw else {}
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		return widget(self, **widget_kw).inline_pack(**pack_kw)

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Frame':
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self


class Field(Frame):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, **kw)
		self.label = Label(self, text=label).inline_pack(side='left')
		self.b_get = lambda: ''
		self.auto_write: Callable[[], None] = lambda: None

	def read(self):
		v = self.b_get()
		self.set_(v if v or v == 0 else '')

	def get(self):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR

	def set_(self, value):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR
