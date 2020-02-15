from abc import ABC, abstractmethod


class InterfaceMusicStorage(ABC):
	"""
	Interface that will connect playlist to music storages.
	Playlist will behave in same manner, but with different save methods.
	Musics can be store in local database, cloud database or even file.
	"""

	@abstractmethod
	def add(self, music):
		"""
		Method that will add music
		:param music: music file path or binaries
		"""
		pass

	@abstractmethod
	def remove(self, i):
		"""
		Method that will remove music
		:return: music: music file path
		"""
		pass

	@abstractmethod
	def get(self, name):
		"""
		Method that will get a music
		:return music:
		"""
		pass
