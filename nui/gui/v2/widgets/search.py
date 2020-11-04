import tkinter
from typing import Callable, Any, List

from .arch import Frame, PopUp
from .basic import Entry, Listbox, Button
from .. import Style


class Search(Frame):
	def __init__(self, master, values: List = None, parse_method: Callable[[Any], str] = lambda v: repr(v), auto_width: bool = True, min_width: int = 1, height: int = 10, selectmode='single', highlightthickness: int = 0, style: Style = None, **kw):
		super().__init__(master, style, **kw)
		self.parse_method = parse_method
		self.v_search = tkinter.StringVar()
		self.v_search.trace_add("write", lambda *args: self.__filter())
		self.search = Entry(self, textvariable=self.v_search).inline_pack()
		self.listbox = Listbox(self, parse_method=parse_method, auto_width=auto_width, min_width=min_width, height=height, selectmode=selectmode, highlightthickness=highlightthickness).inline_pack()
		self.values: List = values if values else []
		self.__filter()

	def set_values(self, value: List):
		self.values = value
		self.__filter()

	def set_(self, value) -> None:
		self.listbox.set_(value)

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
		self.listbox.set_values(out)


class SearchPopUp(PopUp):
	def __init__(self, master, stage, close, style: Style = None, whisper=None, parse_method: Callable[[Any], str] = lambda v: repr(v), auto_width: bool = True, min_width: int = 1, height: int = 10, selectmode='single', highlightthickness: int = 0, **kw):
		super().__init__(master, stage, close, style, whisper, **kw)
		Search(self, whisper, parse_method, auto_width, min_width, height, selectmode, highlightthickness, style, **kw) \
			.inline_select_bind(self.selected) \
			.inline_pack()

	def selected(self, value):
		self.whisper = value
		self.close()


class SearchButton(Button):
	def __init__(self, master, values: List = None, title: str = '', parse_method: Callable[[Any], str] = lambda v: repr(v), auto_width: bool = True, min_width: int = 1, height: int = 10, selectmode='single', highlightthickness: int = 0, popup_style: Style = None, style: Style = None, **kw):
		super().__init__(master, self.__pop, '', style, **kw)
		self.title = title
		self.parse_method = parse_method
		self.auto_width = auto_width
		self.min_width = min_width
		self.height = height
		self.selectmode = selectmode
		self.highlightthickness = highlightthickness
		self.popup_style = popup_style

		self.__values: List = values if values else []
		self.__selected = None

	def __pop(self):
		self.stage.frame_popup(
			SearchPopUp, self.title, self.set_, self.__values, style=self.popup_style,
			parse_method=self.parse_method, auto_width=self.auto_width, min_width=self.min_width, height=self.height, selectmode=self.selectmode, highlightthickness=self.highlightthickness
		)

	def select_index(self, index: int) -> 'SearchButton':
		self.__selected = self.__values[index]
		super().set_(self.__selected)
		return self

	def get_(self):
		return self.__selected if isinstance(self.__selected, List) else [self.__selected]

	def set_(self, value) -> None:
		self.__selected = value
		super().set_(self.__selected)
