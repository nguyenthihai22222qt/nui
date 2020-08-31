import tkinter
from typing import Callable, Any, List

from .arch import Frame
from .imethods import IMethods
from .. import Style


class CheckBoxButtonGroup(Frame, IMethods):
	class CheckBoxButton(tkinter.Checkbutton, IMethods):
		def __init__(self, master, text: str, command: Callable = lambda: None, style: Style = None, **kw):
			self.stage = master.stage
			self.style: Style = style if style else master.style
			self.v = tkinter.IntVar()
			super().__init__(master, text=text, command=command, variable=self.v, bg=self.style.bg, fg=self.style.fg, font=self.style.font, selectcolor=self.style.bg, activebackground=self.style.bg, activeforeground=self.style.fg, **kw)

		def get_(self):
			return self['text']

		def set_(self, value) -> None:
			self['text'] = value

		def is_selected(self):
			return self.v.get()

	def __init__(self, master, parse_method: Callable[[Any], str] = lambda v: repr(v), style: Style = None, **kw):
		super().__init__(master, style=style, **kw)
		self._parse_method = parse_method
		self._values = []
		self._buttons: List[CheckBoxButtonGroup.CheckBoxButton] = []

	def get_(self):
		return [self._values[i] for i, b in enumerate(self._buttons) if b.is_selected()]

	def set_(self, value: List) -> None:
		[x.destroy() for x in self._buttons]
		self._buttons = []
		self._values = value
		for v in value:
			self._buttons.append(CheckBoxButtonGroup.CheckBoxButton(self, text=self._parse_method(v)).inline_pack())

	def select(self, values: List[int]):
		for v in values:
			self._buttons[self._values.index(v)].select()

	def inline_set_and_select(self, set_: List, select: List[int]) -> 'CheckBoxButton':
		self.set_(set_)
		self.select(select)
		return self


class RadioButtonGroup(Frame, IMethods):
	class RadioButton(tkinter.Radiobutton, IMethods):
		def __init__(self, master, variable: tkinter.Variable, text: str, value, command: Callable = lambda: None, style: Style = None, **kw):
			self.stage = master.stage
			self.style: Style = style if style else master.style
			super().__init__(master, text=text, command=command, variable=variable, value=value, bg=self.style.bg, fg=self.style.fg, font=self.style.font, selectcolor=self.style.bg, activebackground=self.style.bg, activeforeground=self.style.fg, **kw)

		def get_(self):
			return self['text']

		def set_(self, value) -> None:
			self['text'] = value

	def __init__(self, master, parse_method: Callable[[Any], str] = lambda v: repr(v), style: Style = None, **kw):
		super().__init__(master, style=style, **kw)
		self._v = tkinter.Variable()
		self._parse_method = parse_method
		self._buttons: List[RadioButtonGroup.RadioButton] = []

	def get_(self):
		return self._v.get()

	def set_(self, value: List) -> None:
		[x.destroy() for x in self._buttons]
		self._buttons = []
		self._v = tkinter.Variable(value=value[0] if value else None)
		for v in value:
			self._buttons.append(RadioButtonGroup.RadioButton(self, variable=self._v, text=self._parse_method(v), value=v).inline_pack())

	def select(self, value):
		self._v.set(value)

	def inline_set_and_select(self, set_: List, select) -> 'RadioButton':
		self.set_(set_)
		self.select(select)
		return self
