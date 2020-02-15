
from players.wav_player import WAVPlayer, WAVWrongTypeError, WAVFileNotLoaded
import pytest as pt
import os

PATH_MUSIC_TESTS = './rebola_pai.wav'
should_test = os.path.exists(PATH_MUSIC_TESTS)


def test_should_instantiate():
	player = WAVPlayer()
	assert isinstance(player, WAVPlayer)


def test_should_not_found_file():
	player = WAVPlayer()
	with pt.raises(FileNotFoundError):
		player.load("./notfound.wav")


@pt.mark.skipif(should_test is False, reason='Project doesnt contain test music')
def test_should_process_only_wav():
	player = WAVPlayer()
	with pt.raises(WAVWrongTypeError):
		player.load("./rebola_pai.mp3")


@pt.mark.skipif(should_test is False, reason='Project doesnt contain test music')
def test_should_found_file():
	player = WAVPlayer()
	player.load(PATH_MUSIC_TESTS)


@pt.mark.skipif(should_test is False, reason='Project doesnt contain test music')
def test_should_not_play_sound():
	player = WAVPlayer()
	with pt.raises(FileNotFoundError):
		player.load("./notfound.wav")
	with pt.raises(WAVFileNotLoaded):
		player.play()


@pt.mark.skipif(should_test is False, reason='Project doesnt contain test music')
def test_should__play_sound():
	player = WAVPlayer()
	player.load(PATH_MUSIC_TESTS)
	player.play()
	assert player._is_active


@pt.mark.skipif(should_test is False, reason='Project doesnt contain test music')
def test_should__play_sound():
	player = WAVPlayer()
	player.load(PATH_MUSIC_TESTS)
	player.play()
	player.stop()
	assert player._is_active is False
