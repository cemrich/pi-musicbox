import os
import vlc

class Player:

	def __init__(self):
		self._instance = vlc.Instance("--no-video")

		self._player = self._instance.media_player_new()

		self._list_player = self._instance.media_list_player_new()
		self._list_player.set_media_player(self._player)

		event_manager = self._list_player.event_manager()
		event_manager.event_attach(vlc.EventType.MediaListPlayerNextItemSet, self._on_next_item_set)

	def set_volume(self, volume):
		self._vlc_volume = (int) (volume * 100)
		self._player.audio_set_volume(self._vlc_volume)

	def play(self, filePath):
		# TODO: error handling

		if os.path.isdir(filePath):
			all_files = [os.path.join(filePath, f) for f in os.listdir(filePath)]
			all_files = sorted(filter(lambda f: os.path.isfile(f), all_files))

			self._play(all_files)
		else:
			self._play([filePath])

	def stop(self):
		self._list_player.stop()

	def _play(self, all_files):
		media_list = self._instance.media_list_new(all_files)
		self._list_player.set_media_list(media_list)
		self._list_player.play()

	def _on_next_item_set(self, event):
		# reset volume to avoid vlc bug
		self._player.audio_set_volume(self._vlc_volume)
