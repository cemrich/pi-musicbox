import os
import math
import vlc

class Player:

	def __init__(self):
		self._instance = vlc.Instance("--no-video")

		self._player = self._instance.media_player_new()

		self._list_player = self._instance.media_list_player_new()
		self._list_player.set_media_player(self._player)

		event_manager = self._player.event_manager()
		event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self._on_item_ended)

	def play(self, filePath, progress=0):
		# TODO: error handling

		if os.path.isdir(filePath):
			all_files = [os.path.join(filePath, f) for f in os.listdir(filePath)]
			all_files = sorted(filter(lambda f: os.path.isfile(f), all_files))

			self._play(all_files, progress)
		else:
			self._play([filePath], progress)

	def stop(self):
		self._list_player.stop()

	def get_progress(self):
		return (self._playlist_index + self._player.get_position()) / self._playlist_size

	def _play(self, all_files, progress):
		print("playing at %f: %s" % (progress, all_files))

		self._playlist_size = len(all_files)
		self._playlist_index = math.floor(self._playlist_size * progress)

		media_list = self._instance.media_list_new(all_files)
		self._list_player.set_media_list(media_list)
		self._list_player.play_item_at_index(self._playlist_index)

		item_progress = self._playlist_size * progress - self._playlist_index
		self._player.set_position(item_progress)

	def _on_item_ended(self, event):
		self._playlist_index += 1
