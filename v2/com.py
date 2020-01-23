from typing import List


class Com:
	def __init__(self, name: List[str], method: callable, man: str = ''):  # TODO name str
		self.name: List[str] = name
		self.method: callable = method
		self.man = man  # TODO Better help
