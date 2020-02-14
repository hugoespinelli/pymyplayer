import tkinter as tk
from thread_player import ThreadPlayer
from players.players_factory import PlayerFactory
from tkinter import filedialog
from utils import get_file_extension

WIDTH = 400
HEIGHT = 100

is_audio_loaded = False
player = None

def render():

	window = tk.Tk()

	window.title("Pymp3 player")

	window.geometry('{}x{}'.format(WIDTH, HEIGHT))

	thread = ThreadPlayer()

	play_btn = tk.Button(window, text='Play', command=lambda: thread.run(ThreadPlayer.PLAY, player), state=tk.DISABLED)
	stop_btn = tk.Button(window, text='Stop', command=lambda: thread.run(ThreadPlayer.STOP, player), state=tk.DISABLED)
	pause_btn = tk.Button(window, text='Pause', command=lambda: thread.run(ThreadPlayer.PAUSE, player), state=tk.DISABLED)
	load_btn = tk.Button(window, text='Load', command=lambda: browse_audio([play_btn, stop_btn, pause_btn]))

	play_btn.grid(row=0, column=0, padx=10, pady=1)
	pause_btn.grid(row=0, column=1, padx=10, pady=1)
	stop_btn.grid(row=0, column=2, padx=10, pady=1)
	load_btn.grid(row=0, column=4, padx=10, pady=1)

	window.mainloop()


def browse_audio(btns):
	global is_audio_loaded, player
	folder_path = filedialog.askopenfilename(
		initialdir='./',
		filetypes=(("wav files", "*.wav"),("mp3 files", "*.mp3"))
	)

	is_audio_loaded = True
	extension = get_file_extension(folder_path)
	player = PlayerFactory.create(extension)
	player.load(folder_path)

	active_button(btns)


def active_button(btns):
	for btn in btns:
		btn['state'] = tk.ACTIVE
