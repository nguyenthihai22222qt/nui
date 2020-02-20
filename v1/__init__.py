from .style import Style
from .widgets import *


class Stage(tkinter.Frame):
	def __init__(self, style: Style):
		super().__init__(tkinter.Tk(), bg=style.bg)
		self.style = style

	def run(self):
		self.master.mainloop()


class Scene(tkinter.Frame):
	def __init__(self, stage: Stage):
		super().__init__(stage, bg=stage.style.bg)
		self.stage: stage = stage
