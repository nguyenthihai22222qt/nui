import tkinter
from typing import Callable, Any, List

from .arch import Frame
from .basic import Entry, Listbox
from .. import Style


class Search(Frame):
	def __init__(self, master, parse_method: Callable[[Any], str] = lambda v: repr(v), auto_width: bool = True, min_width: int = 1, height: int = 10, selectmode='single', highlightthickness: int = 0, style: Style = None, **kw):
		super().__init__(master, style, **kw)
		self.values = []
		self.parse_method = parse_method
		self.v_search = tkinter.StringVar()
		self.v_search.trace_add("write", lambda *args: self.__filter())
		self.search = Entry(self, textvariable=self.v_search).inline_pack()
		self.listbox = Listbox(self, parse_method=parse_method, auto_width=auto_width, min_width=min_width, height=height, selectmode=selectmode, highlightthickness=highlightthickness).inline_pack()

	def set_(self, value: List):
		self.values = value
		self.__filter()

	def get_(self):
		self.listbox.get_()

	def add_items(self, value):
		self.values += value
		self.__filter()

	def inline_select_bind(self, callback: Callable[[Any], None]) -> 'Search':
		self.listbox.inline_select_bind(callback)
		return self

	def __filter(self):  # TODO Move this to Listbox
		out = []
		for v in self.values:
			f = self.parse_method(v)
			if tkinter.re.match(r'.*{}.*'.format(tkinter.re.escape(self.search.get_())), f, tkinter.re.IGNORECASE):
				out.append(v)
		self.listbox.set_(out)
