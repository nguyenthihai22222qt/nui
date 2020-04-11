from typing import Type, Callable, Any

from .arch import Frame, Field
from .basic import Entry, Text


class Form(Frame):
	def __init__(self, master, **kw):
		super().__init__(master, **kw)
		self._fields = {}
		self.auto_write: Callable[[], None] = lambda: None

	def set_auto_write(self, auto_write: Callable[[], None] = lambda: None):
		self.auto_write = auto_write
		return self

	def add_field(self, name: Any, field: Type[Field], label: str, bind_get: Callable[[], str] = lambda: None, **kw):
		f = field(self, label, **kw)
		f.b_get = bind_get
		f.auto_write = self.auto_write
		self._fields[name] = f
		self._fields[name].pack(fill='x')
		return self

	def set_fields(self):
		for field in self._fields.values():
			field.read()
		return self

	def __getitem__(self, item):
		return self._fields[item].get()


class EntryField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Entry(self, width=1)
		self.input.bind('<KeyRelease>', lambda _: self.auto_write())
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
		self.input.bind('<KeyRelease>', lambda _: self.auto_write())
		self.input.pack(side='right', fill='x', expand=True)

	def get(self):
		return self.input.get(1.0, 'end').strip()

	def set_(self, value):
		value = value if value else ''
		self.input.delete(1.0, 'end')
		self.input.insert('end', value)
