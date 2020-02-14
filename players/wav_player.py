from interfaces.interface_sound import InterfaceSound
import simpleaudio as sa
import wave
import re


class WAVWrongTypeError(Exception):
	pass


class WAVFileNotLoaded(Exception):
	pass


class WAVPlayer(InterfaceSound):
	"""
	Class that interact with wav extensions audio files
	"""

	def __init__(self):
		self._wave_read = None
		self._wave = None
		self._play_buffer = None
		self._player = None
		self._total_length_in_seconds = 0
		self._is_active = False

	def load(self, file_path):
		if not self._is_wav_format(file_path):
			raise WAVWrongTypeError()
		self._wave_read = wave.open(file_path, 'rb')
		self._name = self._get_sound_name(file_path)
		self._total_length_in_seconds = self._wave_read.getframerate() / self._wave_read.getnframes()
		self._wave = sa.WaveObject.from_wave_read(self._wave_read)

	def play(self):
		if self._wave is None:
			raise WAVFileNotLoaded

		self._play_buffer = self._wave.play()
		self._is_active = True

	def stop(self):
		if self._is_active:
			self._is_active = False
			self._play_buffer.stop()

	def pause(self):
		pass

	def show_info(self):
		print('play')

	def _get_sound_name(self, path):
		pattern = r'\/(.+)\.\w+'
		matches = re.search(pattern, path)
		if matches is None:
			return None
		return matches.group(1)

	def _is_wav_format(self, path):
		paths = path.split(".")[::-1]

		if len(paths) == 0:
			return False

		if paths[0] == 'wav':
			return True

		return False

