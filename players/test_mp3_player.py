
from players.mp3_player import MP3Player, MP3WrongTypeError, MP3FileNotLoaded
import pytest as pt
import pygame as pg

contains_audio_driver = False
try:
	pg.mixer.init()
	contains_audio_driver = True
except:
	print('Tests wont run because Operational system doesnt have an audio driver!')


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should_instantiate():
	player = MP3Player()
	assert isinstance(player, MP3Player) is True


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should_not_found_file():
	player = MP3Player()
	with pt.raises(FileNotFoundError):
		player.load("./notfound.mp3")
	assert player._playback is None


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should_process_only_mp3():
	player = MP3Player()
	with pt.raises(MP3WrongTypeError):
		player.load("./rebola_pai.wav")


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should_found_file():
	player = MP3Player()
	player.load("./rebola_pai.mp3")


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should_not_play_sound():
	player = MP3Player()
	with pt.raises(FileNotFoundError):
		player.load("./notfound.mp3")
	with pt.raises(MP3FileNotLoaded):
		player.play()


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should__play_sound():
	player = MP3Player()
	player.load("./rebola_pai.mp3")
	player.play()
	assert player._is_playing


@pt.mark.skipif(contains_audio_driver is False, reason='Audio driver not found')
def test_should__play_sound():
	player = MP3Player()
	player.load("./rebola_pai.mp3")
	player.play()
	player.stop()
	assert player._is_playing is False
