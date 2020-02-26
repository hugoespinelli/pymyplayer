
class Music:

	def __init__(self, path):
		self.path = path
		self.name = path.split("/")[::-1][0].split(".")[0]


class Playlist:

	def __init__(self):
		self._musics = []
		self._index_play = 0

	def add(self, music, i=0):
		self._musics.insert(i, music)

	def remove(self, music):
		self._musics.remove(music)

	def show(self):
		return self._musics

	def play(self):
		music = self._musics[self._index_play % len(self._musics)]
		self._index_play += 1

		return music

