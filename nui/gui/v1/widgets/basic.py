import tkinter
from typing import Callable, List, Any

from .imethods import IMethods
from .. import Style


class Label(tkinter.Label, IMethods):
	def __init__(self, master, text: str = '', style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, text=text, bg=self.style.bg, fg=self.style.fg, font=self.style.font, **kw)

	def get_(self):
		return self['text']

	def set_(self, value):
		self['text'] = value


class Button(tkinter.Button, IMethods):
	def __init__(self, master, command: Callable, text: str = '', style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, text=text, bg=self.style.bg, fg=self.style.fg, font=self.style.font, command=command, **kw)

	def get_(self):
		return self['text']

	def set_(self, value) -> None:
		self['text'] = value


class Entry(tkinter.Entry, IMethods):
	def __init__(self, master, width: int = 1, style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, width=width, bg=self.style.bg, fg=self.style.fg, insertbackground=self.style.fg, font=self.style.font, **kw)

	def get_(self):
		return self.get()

	def set_(self, value):
		self.delete(0, 'end')
		self.insert('end', value)


class Text(tkinter.Text, IMethods):
	def __init__(self, master, width: int = 1, height: int = 1, style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, width=width, height=height, bg=self.style.bg, fg=self.style.fg, insertbackground=self.style.fg, font=self.style.font, **kw)

	def get_(self):
		return self.get(1.0, 'end').strip()

	def set_(self, value):
		self.delete(1.0, 'end')
		self.insert('end', value)


class Listbox(tkinter.Listbox, IMethods):
	def __init__(self, master, parse_method: Callable[[Any], str] = lambda v: repr(v), min_width: int = 1, height: int = 10, auto_width: bool = True, highlightthickness: int = 0, style: Style = None, **kw):
		self.stage = master.stage
		self.style: Style = style if style else master.style
		super().__init__(master, width=min_width, height=height, selectmode='single', highlightthickness=highlightthickness, bg=self.style.bg, fg=self.style.fg, font=self.style.font, **kw)
		self._parse_method = parse_method
		self.min_width = min_width
		self.auto_width = auto_width
		self._values = []

	def get_(self):
		s = self.selected()
		return s if s else self.activated()

	def set_(self, value: List) -> None:
		self.delete(0, 'end')
		self._values = value
		width = self.min_width
		for v in value:
			f = self._parse_method(v)
			self.insert('end', f)
			if self.auto_width and len(f) > width:
				width = len(f)
		self.config(width=int(width * 0.9))

	def inline_select_bind(self, callback: Callable[[Any], None]) -> 'Listbox':
		def bind_event(v):
			if v:
				callback(v)

		self.bind("<Return>", lambda _: bind_event(self.activated()))
		self.bind("<<ListboxSelect>>", lambda _: bind_event(self.selected()))
		return self

	def selected(self):  # Selected by mouse
		# self.focus_set() # TODO Idk why this is here. Delete me if everything works
		if self.curselection() != ():
			return self._values[self.curselection()[0]]

	def activated(self):  # Selected by <Return>
		return self._values[self.index('active')]
