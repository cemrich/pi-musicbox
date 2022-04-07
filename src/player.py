import os
import math
import vlc

class Player:

	def __init__(self):
		self._instance = vlc.Instance("--no-video")

		self._player = self._instance.media_player_new()

		self._list_player = self._instance.media_list_player_new()
		self._list_player.set_media_player(self._player)

		self._playlist_size = 0
		self._playlist_index = 0

		event_manager = self._player.event_manager()
		event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self._on_item_ended)


	def set_volume(self, volume):
		"""
		@param volume in percent; between 0 and 100
		"""
		self._player.audio_set_volume(volume)

	def play(self, files, progress=0):
		if (len(files) > 0):
			self._play(files, progress)

	def stop(self):
		self._list_player.stop()

	def next(self):
		if not self._is_playing():
			return

		if self._playlist_index >= self._playlist_size - 1:
			return

		next_result = self._list_player.next()
		if next_result == 0:
			self._change_playlist_index(1)
			print("next: %d" % self._playlist_index)

	def prev(self):
		if not self._is_playing():
			return

		prev_result = self._list_player.previous()
		if prev_result == 0:
			self._change_playlist_index(-1)
			print("prev: %d" % self._playlist_index)

	def get_progress(self):
		if self._playlist_size == 0:
			return 0
		else:
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

	def _is_playing(self):
		return self._player.is_playing()

	def _on_item_ended(self, event):
		self._change_playlist_index(1)

	def _change_playlist_index(self, change):
		self._playlist_index += change
		self._playlist_index = max(0, min(self._playlist_size - 1, self._playlist_index))
