from typing import Type, Callable, Any

from .arch import Frame, Field
from .basic import Entry, Text, Label


class Form(Frame):
	def __init__(self, master, **kw):
		"""
		Container for Fields. Also have some tools for quick get/set for values of objects.\n
		:param master: Parent widget
		:param kw: Other tkinter options
		"""
		super().__init__(master, **kw)
		self._fields = {}
		self.auto_write: Callable[[], None] = lambda: None

	def set_auto_write(self, auto_write: Callable[[], None] = lambda: None) -> 'Form':
		"""
		Sets method for auto_write.
		:param auto_write: Will be automatically binded to every field on '<KeyRelease>' event
		:return: self
		"""
		self.auto_write = auto_write
		return self

	def add_field(self, name: Any, field: Type[Field], label: str, bind_get: Callable[[], str] = lambda: None, **kw) -> 'Form':
		"""
		Add field.\n
		:param name: Key used in __getitem__() (str type is recommended)
		:param field: Class of field
		:param label: Sets the label of field
		:param bind_get: The return from this method will be used as field's value
		:param kw: Other tkinter options (parsed to field).
		:return: self
		"""
		f = field(self, label, **kw)
		f.b_get = bind_get
		f.auto_write = self.auto_write
		self._fields[name] = f.inline_pack(fill='x')
		return self

	def set_fields(self) -> 'Form':
		"""
		Updates all fields based on their bind_get() method.\n
		:return: self
		"""
		for field in self._fields.values():
			field.set_field()
		return self

	def __getitem__(self, item: Any):
		"""
		Returns value of Field by name.\n
		:param item: Name/key of the field
		:return: Field value
		"""
		return self._fields[item].get()


class EntryField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Entry(self, width=1).inline_pack(side='right', fill='x', expand=True)
		self.input.bind('<KeyRelease>', lambda _: self.auto_write())

	def get(self):
		return self.input.get()

	def set_(self, value):
		self.input.delete(0, 'end')
		self.input.insert('end', value)


class TextField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.input = Text(self, width=1, height=2).inline_pack(side='right', fill='x', expand=True)
		self.input.bind('<KeyRelease>', lambda _: self.auto_write())

	def get(self):
		return self.input.get(1.0, 'end').strip()

	def set_(self, value):
		self.input.delete(1.0, 'end')
		self.input.insert('end', value)


class LabelField(Field):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, label, **kw)
		self.this = Label(self).inline_pack(side='right', fill='x', expand=True)

	def get(self):
		return self.this['text']

	def set_(self, value):
		self.this['text'] = value
