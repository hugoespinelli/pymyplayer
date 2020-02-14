from abc import ABC, abstractmethod


class InterfaceSound(ABC):
	"""
	Interface that interact with all format players.
	If you would like to extend to other formats, use this.
	"""

	@abstractmethod
	def load(self, file):
		"""
		Method that will be passed the file path to load audio file
		:param file: file path
		"""
		pass

	@abstractmethod
	def play(self):
		"""
		Method that will be played when user call play button
		:return:
		"""
		pass

	@abstractmethod
	def stop(self):
		"""
		Method that will be played when user call stop button
		:return:
		"""
		pass

	@abstractmethod
	def pause(self):
		"""
		Method that will be played when user call pause button
		:return:
		"""
		pass

	@abstractmethod
	def show_info(self):
		"""
		Method needed to show information about audio file. They are:
		- Filename
		- File size
		- Audio length (HH:MM:SS format)
		- Audio pointer
		:return:
		"""
		pass