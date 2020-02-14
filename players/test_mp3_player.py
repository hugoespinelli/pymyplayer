
from players.mp3_player import MP3Player, MP3WrongTypeError, MP3FileNotLoaded
import pytest as pt


# def test_should_instantiate():
# 	player = MP3Player()
# 	assert isinstance(player, MP3Player) is True
#
#
# def test_should_not_found_file():
# 	player = MP3Player()
# 	with pt.raises(FileNotFoundError):
# 		player.load("./notfound.mp3")
# 	assert player._playback is None
#
#
# def test_should_process_only_mp3():
# 	player = MP3Player()
# 	with pt.raises(MP3WrongTypeError):
# 		player.load("./rebola_pai.wav")
#
#
# def test_should_found_file():
# 	player = MP3Player()
# 	player.load("./rebola_pai.mp3")
#
#
# def test_should_not_play_sound():
# 	player = MP3Player()
# 	with pt.raises(FileNotFoundError):
# 		player.load("./notfound.mp3")
# 	with pt.raises(MP3FileNotLoaded):
# 		player.play()
#
#
# def test_should__play_sound():
# 	player = MP3Player()
# 	player.load("./rebola_pai.mp3")
# 	player.play()
# 	assert player._is_playing
#
#
# def test_should__play_sound():
# 	player = MP3Player()
# 	player.load("./rebola_pai.mp3")
# 	player.play()
# 	player.stop()
# 	assert player._is_playing is False
