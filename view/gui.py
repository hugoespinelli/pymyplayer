import tkinter as tk
from thread_player import ThreadPlayer
from players.players_factory import PlayerFactory
from tkinter import filedialog
from utils import get_file_extension
from playlist import Playlist, Music

WIDTH = 400
HEIGHT = 100

is_audio_loaded = False
player = None
playlist = None

def render():

	window = tk.Tk()

	window.title("Pymp3 player")

	window.geometry('{}x{}'.format(WIDTH, HEIGHT))

	thread = ThreadPlayer()

	playlist_label = tk.Label(window, justify='left')

	play_btn = tk.Button(window, text='Play', command=lambda: thread.run(ThreadPlayer.PLAY, player), state=tk.DISABLED)
	stop_btn = tk.Button(window, text='Stop', command=lambda: thread.run(ThreadPlayer.STOP, player), state=tk.DISABLED)
	pause_btn = tk.Button(window, text='Pause', command=lambda: thread.run(ThreadPlayer.PAUSE, player), state=tk.DISABLED)
	next_btn = tk.Button(window, text='>>', command=lambda: next_music_playlist(), state=tk.DISABLED)
	load_btn = tk.Button(window, text='Load', command=lambda: browse_audio([play_btn, stop_btn, pause_btn, next_btn]))
	make_playlist_btn = tk.Button(window, text='Make Playlist', command=lambda: load_playlist(window, [play_btn, stop_btn, pause_btn, next_btn], playlist_label))

	play_btn.grid(row=0, column=0, padx=2, pady=1)
	pause_btn.grid(row=0, column=1, padx=2, pady=1)
	stop_btn.grid(row=0, column=2, padx=2, pady=1)
	next_btn.grid(row=0, column=3, padx=2, pady=1)
	load_btn.grid(row=0, column=4, padx=2, pady=1)
	make_playlist_btn.grid(row=0, column=4, padx=0, pady=1)

	playlist_label.grid(row=2, column=0, columnspan=5, pady=3)

	window.mainloop()


def next_music_playlist():
	load_player(playlist.play().path)


def load_playlist(window, btns, label):
	global playlist
	folder_path = filedialog.askopenfilenames(
		parent=window,
		initialdir='./',
		filetypes=(("wav files", "*.wav"),("mp3 files", "*.mp3"))
	)
	paths_list = window.tk.splitlist(folder_path)
	if len(paths_list) == 0:
		return
	musics = [ Music(path) for path in paths_list ]
	playlist = create_playlist(musics)

	label['text'] = mount_playlist_text(playlist)

	load_player(playlist.play().path)

	active_button(btns)


def create_playlist(musics):
	playlist = Playlist()
	for music in musics:
		playlist.add(music)
	return playlist


def mount_playlist_text(playlist):
	musics = playlist.show()
	label = ''
	for index, music in enumerate(musics):
		label += '{} - {} \n'.format(index+1, music.name[:30])
	return label


def browse_audio(btns):
	global is_audio_loaded, player
	folder_path = filedialog.askopenfilename(
		initialdir='./',
		filetypes=(("wav files", "*.wav"),("mp3 files", "*.mp3"))
	)

	load_player(folder_path)

	active_button(btns)


def load_player(path):
	global is_audio_loaded, player

	is_audio_loaded = True
	extension = get_file_extension(path)
	player = PlayerFactory.create(extension)
	player.load(path)


def active_button(btns):
	for btn in btns:
		btn['state'] = tk.ACTIVE
