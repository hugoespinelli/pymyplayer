from playlist import Music


def test_should_instantiate_music():
	music = Music('./test.mp3')
	assert isinstance(music, Music)


def test_should_separate_name_file():
	music = Music('./test.mp3')
	assert music.name == 'test'
