from typing import List, Union

from .com import Com
from .shell import Shell


# noinspection PyMethodMayBeStatic
class Api:
	def __init__(self):
		self.shell: Union[Shell, None] = None

	def get_commands(self) -> List[Com]:
		# Overwrite me
		return []

	def run(self):  # TODO Maybe run one command
		if not self.shell:
			self.shell = Shell(self)
		print("Running TODO")
