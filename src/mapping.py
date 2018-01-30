import os
import player

class MappedPlayer:

	def __init__(self):
		self._files_dir = os.path.join(os.path.dirname(__file__), "..", "files")
		self._player = player.Player()

	def set_volume(self, volume):
		self._player.set_volume(volume)

	def play(self, id):
		self._player.play(os.path.join(self._files_dir, id))

	def stop(self):
		self._player.stop()
