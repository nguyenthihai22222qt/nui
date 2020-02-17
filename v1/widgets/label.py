from tkinter import Label as tkLabel

from v1._widget import _Widget
from v1.style import Style


class Label(_Widget, tkLabel):
	def __init__(self, master, style: Style, **kw):
		tkLabel.__init__(self, master, **style.quick(bg=True, fg=True), **kw)
		_Widget.__init__(self, style)
