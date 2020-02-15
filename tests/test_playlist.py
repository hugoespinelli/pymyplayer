from playlist import Playlist, Music


def test_should_instantiate_playlist():
	playlist = Playlist()
	assert isinstance(playlist, Playlist)


def test_should_add_music():
	playlist = Playlist()
	playlist.add('./rebola_pai.mp3')
	assert playlist._musics[0].name == 'rebola_pai'

