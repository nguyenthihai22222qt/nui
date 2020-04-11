import tkinter

from .basic import Label


class Frame(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def add(self, widget, widget_kw=None, pack_kw=None):
		widget_kw = widget_kw if widget_kw else {}
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, **widget_kw).pack(**pack_kw)
		return self


class Field(Frame):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, **kw)
		self.label = Label(self, text=label)
		self.label.pack(side='left')
		self.b_get = lambda: None
		self.b_set = lambda v: None
		self.auto_write: bool = False

	def value_change_event(self, _=None):  # TODO Test how many times this calls write/read
		if self.auto_write:
			self.write()
			self.read()

	def write(self):
		self.b_set(self.get())

	def read(self):
		self.set_(self.b_get())

	def get(self):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR

	def set_(self, value):
		raise Exception(f"Get method of field f{self.__class__}: {self.label['text']}")  # NOSONAR
