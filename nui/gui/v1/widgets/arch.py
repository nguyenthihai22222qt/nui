import tkinter
from typing import Type

from .basic import IMethods
from .. import Style


class Frame(tkinter.Frame, IMethods):
	def __init__(self, master, style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, bg=self.style.bg, **kw)

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
