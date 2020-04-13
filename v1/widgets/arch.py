import tkinter
from typing import Callable, Type

from .basic import IPack, Label


class Frame(tkinter.Frame, IPack):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def inline_add(self, widget: Type[tkinter.Widget], widget_kw: dict = None, pack_kw: dict = None) -> 'Frame':
		"""
		Add widget to this Frame.\n
		:param widget: widget class (not object)
		:param widget_kw: kwargs to pass to widget's __init__
		:param pack_kw: kwargs to pass to widget's pack()
		:return: self
		"""
		widget_kw = widget_kw if widget_kw else {}
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, **widget_kw).pack(**pack_kw)
		return self

	def add(self, widget: Type[tkinter.Widget], widget_kw=None, pack_kw=None) -> tkinter.Widget:  # TODO Is tkinter.Widget correct?
		"""
		Add widget to this Frame.\n
		:param widget: widget class (not object)
		:param widget_kw: kwargs to pass to widget's __init__
		:param pack_kw: kwargs to pass to widget's pack()
		:return: widget
		"""
		widget_kw = widget_kw if widget_kw else {}
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		o = widget(self, **widget_kw)
		o.pack(**pack_kw)  # tkinter doesn't have inline_pack()
		return o


class Field(Frame):
	def __init__(self, master, label: str, **kw):
		"""
		Mainly used in Form.\n
		:param master: Parent widget
		:param label: Description
		:param kw: Other tkinter kwargs
		"""
		super().__init__(master, **kw)
		self.label = Label(self, text=label).inline_pack(side='left')
		self.b_get = lambda: ''
		self.auto_write: Callable[[], None] = lambda: None

	def set_field(self) -> None:
		"""
		Sets field.\n
		"""
		v = self.b_get()
		self.set_(v if v or v == 0 else '')

	def get(self) -> str:
		"""
		Returns field value.\n
		:return: Str
		"""
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR

	def set_(self, value) -> None:
		"""
		Sets field value.\n
		"""
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR
