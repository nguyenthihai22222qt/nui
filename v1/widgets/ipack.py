import tkinter


class IPack(tkinter.Pack):
	def inline_pack(self, /, *, fill='both', side='top', expand=False, **kw):
		"""
		Packs it's self and returns self.\n
		:param fill: Specifies whether the widget should occupy all the space provided to it by the master. If NONE, keep the widget’s original size. If X (fill horizontally), Y (fill vertically), or BOTH (default), fill the given space along that direction. To make a widget fill the entire master widget, set fill to BOTH and expand to a non-zero value.
		:param side: Specifies which side to pack the widget against. To pack widgets vertically, use TOP (default). To pack widgets horizontally, use LEFT. You can also pack widgets along the BOTTOM and RIGHT edges.
		:param expand: Specifies whether the widgets should be expanded to fill any extra space in the geometry master. If false (default), the widget is not expanded.
		:param kw: Other options (see official tkinter.Widget.pack() documentation)
		:return: self
		"""
		self.pack(fill=fill, side=side, expand=expand, **kw)
		return self
