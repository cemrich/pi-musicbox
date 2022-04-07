import vlc
from enum import Enum

class Sfx(Enum):
	START = 0
	PREV = 1
	NEXT = 2
	TAG_DETECTED = 3
	TAG_REMOVED = 4

class SfxPlayer:

	FILES = {
		Sfx.START: "files/start.mp3",
		Sfx.PREV: "files/plop.mp3",
		Sfx.NEXT: "files/plop.mp3",
		Sfx.TAG_DETECTED: "files/plipp.mp3",
		Sfx.TAG_REMOVED: "files/plipp_low.mp3"
	}

	def __init__(self):
		self._instance = vlc.Instance("--no-video")
		self._player = self._instance.media_player_new()

		self._media_dict = dict((sfx, self._instance.media_new(self.FILES[sfx])) for sfx in Sfx)

	def play(self, file):
		self._player.set_media(self._media_dict[file])
		self._player.audio_set_volume(70)
		self._player.play()
