from players.wav_player import WAVPlayer

class PlayerFactory:

	@staticmethod
	def create(extension):
		if extension == 'wav':
			return WAVPlayer()
		return None