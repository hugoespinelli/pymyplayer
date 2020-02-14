
from players.wav_player import WAVPlayer, WAVWrongTypeError, WAVFileNotLoaded
import pytest as pt


def test_should_instantiate():
	player = WAVPlayer()


def test_should_not_found_file():
	player = WAVPlayer()
	with pt.raises(FileNotFoundError):
		player.load("./notfound.wav")


# def test_should_process_only_wav():
# 	player = WAVPlayer()
# 	with pt.raises(WAVWrongTypeError):
# 		player.load("./rebola_pai.mp3")
#
#
# def test_should_found_file():
# 	player = WAVPlayer()
# 	player.load("./rebola_pai.wav")
#
#
# def test_should_not_play_sound():
# 	player = WAVPlayer()
# 	with pt.raises(FileNotFoundError):
# 		player.load("./notfound.wav")
# 	with pt.raises(WAVFileNotLoaded):
# 		player.play()
#
#
# def test_should__play_sound():
# 	player = WAVPlayer()
# 	player.load("./rebola_pai.wav")
# 	player.play()
# 	assert player._is_active
#
#
# def test_should__play_sound():
# 	player = WAVPlayer()
# 	player.load("./rebola_pai.wav")
# 	player.play()
# 	player.stop()
# 	assert player._is_active is False