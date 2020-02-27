import tkinter

from .basic import Label, Entry, Text


class Form(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)
		self._fields = []

	def add_entry(self, label: str):
		self._fields.append(EntryField(self, label))
		self._fields[-1].pack(fill='x', expand=True)
		return self

	def add_text(self, label: str):
		self._fields.append(TextField(self, label))
		self._fields[-1].pack(fill='x', expand=True)
		return self


class EntryField(tkinter.Frame):
	def __init__(self, master, label: str, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)
		self.label = Label(self, text=label)
		self.input = Entry(self, width=1)
		self.label.pack(side='left')
		self.input.pack(side='right', fill='x', expand=True)


class TextField(tkinter.Frame):
	def __init__(self, master, label: str, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)
		self.label = Label(self, text=label)
		self.input = Text(self, width=1, height=2)
		self.label.pack(side='left')
		self.input.pack(side='right', fill='x', expand=True)
