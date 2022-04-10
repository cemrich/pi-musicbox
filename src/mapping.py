import os
import os.path
import player
import persistence
import mediaFileHelper

class MappedPlayer:

	def __init__(self):
		base_dir = os.path.join(os.path.dirname(__file__), "..", "files")
		self._player = player.Player()
		self._file_helper = mediaFileHelper.MediaFileHelper(base_dir)
		self._position_storage = persistence.PositionStorage()
		self._progress = dict()
		self._current_id = ""

	def play(self, id):
		self._current_id = id
		progress = self._get_progress(self._current_id)
		files = self._file_helper.get_files(id)

		if files:
			self._player.play(files, progress)
		else:
			self._file_helper.copy_new(id)
			files = self._file_helper.get_files(id)
			self._player.play(files, progress)

	def set_volume(self, volume):
		"""
		@param volume in percent; between 0 and 100
		"""
		self._player.set_volume(volume)

	def stop(self):
		self._save_progress(self._current_id, self._player.get_progress())
		self._player.stop()

	def next(self):
		self._player.next()

	def prev(self):
		self._player.prev()

	def destroy(self):
		self._position_storage.destroy()

	def _save_progress(self, id, progress):
		print("save playback progress for %s: %f" % (id, progress))
		self._position_storage.save_position(id, progress)

	def _get_progress(self, id):
		progress = self._position_storage.get_position(id)
		return progress if progress > 0 and progress < 1 else 0
