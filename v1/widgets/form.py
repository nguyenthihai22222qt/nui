from typing import Type, Callable

from .arch import Frame, Field
from .basic import Entry, Text


class Form(Frame):
	def __init__(self, master, **kw):
		super().__init__(master, **kw)
		self._fields = []

	def add_field(self, field: Type[Field], label: str, bind_get: Callable[[], str] = lambda: None, bind_set: Callable[[str], None] = lambda v: None, /, *, auto_write: bool = False, **kw):
		f = field(self, label, **kw)
		f.b_get = bind_get
		f.b_set = bind_set
		f.auto_write = auto_write
		self._fields.append(f)
		self._fields[-1].pack(fill='x')
		return self

	def set_fields(self):
		for field in self._fields:
			field.read()
		return self

	def write_fields(self):
		for field in self._fields:
			field.write()


class EntryField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Entry(self, width=1)
		self.input.bind('<KeyRelease>', super().value_change_event)  # TODO Move to Field
		self.input.pack(side='right', fill='x', expand=True)

	def get(self):
		return self.input.get()

	def set_(self, value):
		value = value if value else ''
		self.input.delete(0, 'end')
		self.input.insert('end', value)


class TextField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Text(self, width=1, height=2)
		self.input.bind('<KeyRelease>', super().value_change_event)
		self.input.pack(side='right', fill='x', expand=True)

	def get(self):
		return self.input.get(1.0, 'end').strip()

	def set_(self, value):
		value = value if value else ''
		self.input.delete(1.0, 'end')
		self.input.insert('end', value)
