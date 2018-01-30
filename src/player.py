import os
import vlc

class Player:

	def __init__(self):
		self.instance = vlc.Instance("--no-video")

		self.player = self.instance.media_player_new()

		self.list_player = self.instance.media_list_player_new()
		self.list_player.set_media_player(self.player)

		event_manager = self.list_player.event_manager()
		event_manager.event_attach(vlc.EventType.MediaListPlayerNextItemSet, self._on_next_item_set)

	def setVolume(self, volume):
		self.vlc_volume = (int) (volume * 100)
		self.player.audio_set_volume(self.vlc_volume)

	def play(self, filePath):
		# TODO: error handling

		if os.path.isdir(filePath):
			allFiles = [os.path.join(filePath, f) for f in os.listdir(filePath)]
			allFiles = sorted(filter(lambda f: os.path.isfile(f), allFiles))

			self._play(allFiles)
		else:
			self._play([filePath])

	def stop(self):
		self.list_player.stop()

	def _play(self, allFiles):
		media_list = self.instance.media_list_new(allFiles)
		self.list_player.set_media_list(media_list)
		self.list_player.play()

	def _on_next_item_set(self, event):
		# reset volume to avoid vlc bug
		self.player.audio_set_volume(self.vlc_volume)
