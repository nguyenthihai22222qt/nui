from typing import Type

from .arch import Frame, Field
from .basic import Entry, Text


class Form(Frame):
	def __init__(self, master, **kw):
		super().__init__(master, **kw)
		self._fields = []

	def add_field(self, field: Type[Field], label: str, **kw):
		self._fields.append(field(self, label, **kw))
		self._fields[-1].pack(fill='x', expand=True)
		return self


class EntryField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Entry(self, width=1)
		self.input.pack(side='right', fill='x', expand=True)


class TextField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Text(self, width=1, height=2)
		self.input.pack(side='right', fill='x', expand=True)
