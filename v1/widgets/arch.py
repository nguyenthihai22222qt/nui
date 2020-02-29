import tkinter

from .basic import Label


class Frame(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def add(self, widget, widget_kw=None, pack_kw=None):
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, **widget_kw).pack(**pack_kw)
		return self


class Field(Frame):
	def __init__(self, master, label: str, **kw):
		super().__init__(master, **kw)
		self.label = Label(self, text=label)
		self.label.pack(side='left')
