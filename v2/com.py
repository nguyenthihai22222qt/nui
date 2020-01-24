from typing import List, Union


class Com:
	def __init__(self, name: Union[str, List[str]], method: callable, man: str = ''):
		self.name: List[str] = name if isinstance(name, List) else name.strip().split(' ')
		self.method: callable = method
		self.man = man  # TODO Better help
