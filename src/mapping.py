import os
import player

class MappedPlayer:

	def __init__(self):
		self.filesDir = os.path.join(os.path.dirname(__file__), "..", "files")
		self.player = player.Player()

	def setVolume(self, volume):
		self.player.setVolume(volume)

	def play(self, id):
		self.player.play(os.path.join(self.filesDir, id))

	def stop(self):
		self.player.stop()
