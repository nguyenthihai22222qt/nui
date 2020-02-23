import tkinter

from .basic import Label, Entry, Text
from .. import Style


# TODO Offset everything
# TODO Bind
# TODO Reduce boiler plate
class Form(tkinter.Frame):
	def __init__(self, master, style: Style = None, **kw):
		super().__init__(master, bg=style.bg, **kw)
		self.style = style
		self._fields = []

	def add_entry(self, label: str):
		self._fields.append(EntryField(self, self.style, label))
		self._fields[-1].pack(fill='x', expand=True)
		return self

	def add_text(self, label: str):
		self._fields.append(TextField(self, self.style, label))
		self._fields[-1].pack(fill='x', expand=True)
		return self


class EntryField(tkinter.Frame):
	def __init__(self, master, style: Style, label: str, **kw):
		super().__init__(master, bg=style.bg, **kw)
		self.style = style
		self.label = Label(self, style, text=label)
		self.input = Entry(self, style, width=1)
		self.label.pack(side='left')
		self.input.pack(side='right', fill='x', expand=True)


class TextField(tkinter.Frame):
	def __init__(self, master, style: Style, label: str, **kw):
		super().__init__(master, bg=style.bg, **kw)
		self.style = style
		self.label = Label(self, style, text=label)
		self.input = Text(self, style, width=1, height=2)
		self.label.pack(side='left')
		self.input.pack(side='right', fill='x', expand=True)
