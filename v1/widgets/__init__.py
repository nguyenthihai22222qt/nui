from .basic import *
from .flat_button import *
from .form import *


class Frame(tkinter.Frame):
	def __init__(self, master, **kw):
		self.stage = master.stage
		super().__init__(master, bg=self.stage.style.bg, **kw)

	def add(self, widget, widget_kw=None, pack_kw=None):
		pack_kw = pack_kw if pack_kw else {'fill': 'both'}
		widget(self, self.stage.style, **widget_kw).pack(**pack_kw)
		return self
