import threading


class ThreadPlayer:

	"""
	Class that will start thread processes and call interface sounds
	"""

	PLAY = 'play'
	STOP = 'stop'
	PAUSE = 'pause'

	def __init__(self):
		self.thread = None

	def start(self, func):
		self.thread = threading.Thread(target=func, daemon=True)
		self.thread.start()

	def run(self, command, player):
		player_func = getattr(player, command)

		if command == ThreadPlayer.PLAY and self.thread is not None:
			return

		self.thread = threading.Thread(target=player_func, daemon=True)
		self.thread.start()

		if command == ThreadPlayer.STOP or command == ThreadPlayer.PAUSE:
			self.thread.join()
			self.thread = None

