import os
import player

class MappedPlayer:

	def __init__(self):
		self._files_dir = os.path.join(os.path.dirname(__file__), "..", "files")
		self._player = player.Player()
		self._progress = dict()
		self._current_id = ""

	def set_volume(self, volume):
		self._player.set_volume(volume)

	def play(self, id):
		self._current_id = id

		full_path = os.path.join(self._files_dir, id)
		progress = self._get_progress(id)

		self._player.play(full_path, progress)

	def stop(self):
		self._save_progress(self._current_id, self._player.get_progress())
		self._player.stop()

	def _save_progress(self, id, progress):
		self._progress[id] = progress

	def _get_progress(self, id):
		progress =  self._progress.get(id, 0)
		return progress if progress < 1 else 0
