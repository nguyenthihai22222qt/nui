import tkinter

from .widgets import *


class Stage(tkinter.Frame):
	def __init__(self):
		super().__init__()


class Scene(tkinter.Frame):
	def __init__(self, stage):
		super().__init__(stage)
		self.stage = stage
