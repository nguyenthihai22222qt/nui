from typing import Type, Callable, Any, Dict

from .arch import Frame
from .basic import Label
from .imethods import IMethods


class Form(Frame):
	class _Field(Frame):
		def __init__(self, master, label: str, widget: Type[IMethods], b_get: Callable = lambda: '', auto_write: Callable = lambda: None, **kw):
			super().__init__(master)
			self.label = Label(self, text=label).inline_pack(side='left')
			self.w = widget(self, **kw).inline_bind('<KeyRelease>', lambda _: auto_write()).inline_pack(expand=True)
			self.b_get = b_get

		def get_(self) -> str:
			return self.w.get_()

		def set_(self, value) -> None:
			v = self.b_get()
			self.w.set_(v if v or v == 0 else value)

	def __init__(self, master, **kw):
		"""
		Container for Fields. Also have some tools for quick get/set for values of objects.\n
		:param master: Parent widget
		:param kw: Other tkinter options
		"""
		super().__init__(master, **kw)
		self._fields: Dict[str, Form._Field] = {}
		self.auto_write: Callable[[], None] = lambda: None

	def set_auto_write(self, auto_write: Callable[[], None] = lambda: None) -> 'Form':
		"""
		Sets method for auto_write.
		:param auto_write: Will be automatically binded to every field on '<KeyRelease>' event
		:return: self
		"""
		self.auto_write = auto_write
		return self

	def add_field(self, name: Any, widget: Type[IMethods], label: str, bind_get: Callable[[], str] = lambda: None, **kw) -> 'Form':
		"""
		Add field.\n
		:param name: Key used in __getitem__() (str type is recommended)
		:param widget: Class of field
		:param label: Sets the label of field
		:param bind_get: The return from this method will be used as field's value
		:param kw: Other tkinter options (parsed to field).
		:return: self
		"""
		# noinspection PyProtectedMember
		self._fields[name] = Form._Field(self, label, widget, bind_get, self.auto_write, **kw).inline_pack(fill='x')
		return self

	def set_fields(self) -> 'Form':
		"""
		Updates all fields based on their bind_get() method.\n
		:return: self
		"""
		for f in self._fields.values():
			f.set_('')
		return self

	def __getitem__(self, item: Any):
		"""
		Returns value of _Field by name.\n
		:param item: Name/key of the field
		:return: _Field value
		"""
		return self._fields[item].get_()
