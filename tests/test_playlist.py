from playlist import Playlist, Music


def test_should_instantiate_playlist():
	playlist = Playlist()
	assert isinstance(playlist, Playlist)


def test_should_add_music():
	playlist = Playlist()
	music = Music('./rebola_pai.mp3')
	playlist.add(music)
	assert playlist._musics[0].name == 'rebola_pai'


def test_should_remove_music():
	playlist = Playlist()
	music = Music('./rebola_pai.mp3')
	playlist.add(music)
	playlist.remove(music)
	assert len(playlist._musics) == 0


def test_should_get_first_music():
	playlist = Playlist()
	music = Music('./rebola_pai.mp3')
	playlist.add(music)
	assert playlist.play() == music


def test_should_get_same_music():
	playlist = Playlist()
	music = Music('./rebola_pai.mp3')
	playlist.add(music)
	playlist.play()
	assert playlist.play() == music


def test_should_count_index_playlist():
	playlist = Playlist()
	music = Music('./rebola_pai.mp3')
	playlist.add(music)
	playlist.play()
	playlist.play()
	playlist.play()
	assert playlist._index_play == 3

