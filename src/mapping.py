import os
import player
import persistence

class MappedPlayer:

	def __init__(self):
		self._files_dir = os.path.join(os.path.dirname(__file__), "..", "files")
		self._player = player.Player()
		self._position_storage = persistence.PositionStorage()
		self._progress = dict()
		self._current_id = ""

	def play(self, id):
		self._current_id = id

		full_path = os.path.join(self._files_dir, id)
		progress = self._get_progress(id)

		self._player.play(full_path, progress)

	def stop(self):
		self._save_progress(self._current_id, self._player.get_progress())
		self._player.stop()

	def destroy(self):
		self._position_storage.destroy()

	def _save_progress(self, id, progress):
		self._position_storage.save_position(id, progress)

	def _get_progress(self, id):
		progress = self._position_storage.get_position(id)
		return progress if progress < 1 else 0
