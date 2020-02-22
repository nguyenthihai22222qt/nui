from typing import Union, Dict, Type

from .style import Style
from .widgets import *


class Stage(tkinter.Frame):
	def __init__(self, style: Style):
		super().__init__(tkinter.Tk(), bg=style.bg)
		self.style = style
		self._active: Union['Scene', type] = type("TempScene", (), {'deactivate': lambda: None})
		self._scenes: Dict[str, 'Scene'] = {}

		self.master.bind('<Key>', self._typed)

	def add(self, name: str, scene: Type['Scene']) -> 'Stage':
		"""
		Add scene
		Possible to chain (.add(...).add(...).add(...) you get it).
		:param name: Name/Key of the scene. Automatically converted to lower case.
		:param scene: Class which inherits Scene (class not object)
		:return: Stage (self)
		"""
		self._scenes[name.lower()] = scene(self)
		return self

	def __getitem__(self, name: str) -> 'Scene':
		"""
		Get specific scene. Any other way of getting scenes is discouraged
		:param name: Name/Key of Scene. Automatically converted to lower case.
		:return: Scene object
		"""
		return self._scenes.get(name.lower())

	def _typed(self, event) -> None:
		"""
		This method is not meant to be called manually.
		Fired every time user preses key while window focused.
		And calls active scene typed(event) method
		:param event: tkinter bind <Ket> event
		:return: None
		"""
		self._active.typed(event)

	def switch(self, to: Union['Scene', str]) -> None:
		"""
		Switches scenes. Any other way of switching scenes is discouraged.
		1. Call active scene deactivate() method
		2. Replace active scene with new one (`to` param)
		3. Call activate() on (new) active scene
		(4. Focus active scene)
		:param to: Scene switching to
		:return: None
		"""
		self._active.deactivate()
		self._active = (to if isinstance(to, Scene) else self._scenes.get(to))
		self._active.activate()
		self._active.focus_set()

	def tick(self) -> None:
		"""
		This method is not meant to be called manually.
		Fired every 10 ticks (Number could change).
		:return:
		"""
		self._active.tick()
		self.after(10, self.tick)

	def run(self, scene: Union['Scene', str]) -> None:
		"""
		Call this to show window and run mainloop. Any other way of running mainloop is discouraged.
		:param scene: Scene to show after start
		:return: None
		"""
		self.switch(scene)
		self.master.after(1, self.tick)
		self.master.mainloop()


class Scene(tkinter.Frame):
	def __init__(self, stage: Stage):
		super().__init__(stage, bg=stage.style.bg)
		self.stage: stage = stage

	def tick(self) -> None:
		"""
		Overwrite me
		This method is not meant to be called manually.
		Fired every 10 ticks (Number could change).
		:return: None
		"""
		pass

	def typed(self, event) -> None:
		"""
		Overwrite me
		This method is not meant to be called manually.
		Fired every time user preses key while window focused.
		:param event: tkinter bind <Ket> event
		:return: None
		"""
		pass

	def activate(self) -> None:
		"""
		This method is not meant to be called manually.
		Fired every time this scene is activated/showed.
		This method should pack scene (self.pack()).
		:return: None
		"""
		self.pack(fill='both', expand=True)

	def deactivate(self) -> None:
		"""
		This method is not meant to be called manually.
		Fired when stage is switching to another scene (from this one).
		This method should unpack whole scene. (self.pack_forget())
		:return: None
		"""
		self.pack_forget()
