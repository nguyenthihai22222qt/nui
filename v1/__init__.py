from typing import Union, Dict, Type

from .style import Style
from .widgets import *


class Stage(tkinter.Frame):
	def __init__(self, style: Style):
		super().__init__(tkinter.Tk(), bg=style.bg)
		self.style = style
		self._active: Union['Scene', type] = type("TempScene", (), {'deactivate': lambda: None})
		self._scenes: Dict[str, 'Scene'] = {}

		self.master.bind('<Key>', self.typed)

	def add(self, name: str, scene: Type['Scene']):
		self._scenes[name] = scene(self)
		return self

	def __getitem__(self, item: str):
		return self._scenes.get(item)

	def typed(self, event):
		self._active.typed(event)

	def switch(self, to: 'Scene'):
		self._active.deactivate()
		self._active = to
		self._active.activate()
		self._active.focus_set()

	def tick(self):
		self._active.tick()
		self.after(10, self.tick)

	def run(self, scene: Union['Scene', str]):
		(scene if isinstance(scene, Scene) else self._scenes.get(scene)).switch_to_me()
		self.master.after(1, self.tick)
		self.master.mainloop()


class Scene(tkinter.Frame):
	def __init__(self, stage: Stage):
		super().__init__(stage, bg=stage.style.bg)
		self.stage: stage = stage

	def tick(self) -> None:
		"""
		Overwrite me
		This is called every 10 ticks (Number could change).
		:return: None
		"""
		pass

	def typed(self, event) -> None:
		"""
		Overwrite me
		Fired every time user preses key while window focused.
		:param event: tkinter bind <Ket> event
		:return: None
		"""
		pass

	def activate(self):
		self.pack(fill='both', expand=True)

	def deactivate(self):
		self.pack_forget()

	def switch_to_me(self):
		self.stage.switch(self)
