import pygame as pg
from interfaces.interface_sound import  InterfaceSound
from utils import get_file_extension

pg.mixer.init()

class MP3WrongTypeError(Exception):
	pass


class MP3FileNotLoaded(Exception):
	pass


class MP3Player(InterfaceSound):
	"""
	Class that interact with mp3 extensions audio files
	"""

	def __init__(self):
		self._playback = None
		self._is_playing = False
		self._is_paused = False
		self._file = None

	def load(self, file):
		extension = get_file_extension(file)

		if extension != 'mp3':
			raise MP3WrongTypeError

		try:
			pg.mixer.music.load(file)
		except Exception as e:
			raise FileNotFoundError

		self._file = file

	def play(self):

		if self._file is None:
			raise MP3FileNotLoaded

		self._is_playing = True

		if self._is_paused:
			pg.mixer.music.unpause()
			self._is_paused = False
		else:
			pg.mixer.music.play()

	def stop(self):
		self._is_playing = False
		pg.mixer.music.stop()

	def pause(self):
		self._is_playing = False
		self._is_paused = True
		pg.mixer.music.pause()

	def show_info(self):
		pass
