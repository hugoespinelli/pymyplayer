from players.wav_player import WAVPlayer
from players.mp3_player import MP3Player

class PlayerFactory:

	@staticmethod
	def create(extension):
		if extension == 'wav':
			return WAVPlayer()
		if extension == 'mp3':
			return MP3Player()
		return None
