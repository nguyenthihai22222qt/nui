from typing import Union, Dict, List

from .style import Style
from .widgets import *


class Stage(tkinter.Frame):
	def __init__(self, style: Style):
		super().__init__(tkinter.Tk(), bg=style.bg)
		self.style = style
		self._active: Union['Scene', type] = type("TempScene", (), {'deactivate': lambda: None})
		self._scenes: Dict[str, 'Scene'] = {}

		self.master.bind('<Key>', self._typed)

	def add(self, name: str, scene: Type['Scene'], *args, **kwargs) -> 'Stage':
		"""
		Add scene
		Possible to chain (.add(...).add(...).add(...) you get it).
		:param name: Name/Key of the scene. Automatically converted to lower case.
		:param scene: Class which inherits Scene (class not object)
		:return: Stage (self)
		"""
		self._scenes[name.lower()] = scene(self, *args, **kwargs)
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
		Switches scenes. Any other way of switching scenes is discouraged.\n
		1. Call active scene deactivate() method\n
		2. Replace active scene with new one (`to` param)\n
		3. Call activate() on (new) active scene\n
		(4. Focus active scene)\n
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

	def popup(self, title: str, message: str, options: List[str]):
		root = tkinter.Toplevel()
		root.resizable(False, False)
		root.title(title)
		tkinter.Label(root, text=message, bg=self.style.bg, fg=self.style.fg).pack(fill='both')
		frame = tkinter.Frame(root, bg=self.style.bg)
		out = tkinter.StringVar()

		def on_closing():
			root.destroy()
			root.quit()

		def com(text):
			out.set(text)
			on_closing()

		root.protocol("WM_DELETE_WINDOW", on_closing)
		[tkinter.Button(frame, command=lambda x=x: com(x), text=x, bg=self.style.bg, fg=self.style.fg).pack(fill='both', side='right') for x in options]
		frame.pack(fill='both')
		root.grab_set()
		root.mainloop()
		root.grab_release()
		return out.get()


class Scene(tkinter.Frame):
	def __init__(self, stage: Stage, *args, **kwargs):
		self.stage: Stage = stage
		super().__init__(stage, bg=self.stage.style.bg)

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
