import tkinter
from typing import Callable, Type

from .basic import Label


class Frame(tkinter.Frame):
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

	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw) -> 'Frame':
		"""
		Packs it's self and returns self.\n
		:param fill: Specifies whether the widget should occupy all the space provided to it by the master. If NONE, keep the widget’s original size. If X (fill horizontally), Y (fill vertically), or BOTH (default), fill the given space along that direction. To make a widget fill the entire master widget, set fill to BOTH and expand to a non-zero value.
		:param side: Specifies which side to pack the widget against. To pack widgets vertically, use TOP (default). To pack widgets horizontally, use LEFT. You can also pack widgets along the BOTTOM and RIGHT edges.
		:param expand: Specifies whether the widgets should be expanded to fill any extra space in the geometry master. If false (default), the widget is not expanded.
		:param kw: Other options (see official tkinter.Widget.pack() documentation)
		:return: self
		"""
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self


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

	def read(self) -> None:
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
