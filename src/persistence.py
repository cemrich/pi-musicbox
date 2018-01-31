import os
import sqlite3

class PositionStorage:

	def __init__(self):
		db_dir = os.path.join(os.path.dirname(__file__), "..", "data.db")
		self._conn = sqlite3.connect(db_dir)

		cursor = self._conn.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS Position (id text PRIMARY KEY, position real)")
		self._conn.commit()

	def save_position(self, id, position):
		cursor = self._conn.cursor()
		cursor.execute("REPLACE INTO Position VALUES (?, ?)", (id, position))
		self._conn.commit()

	def get_position(self, id):
		cursor = self._conn.cursor()
		cursor.execute('SELECT position FROM Position WHERE id=?', (id,))

		result_set = cursor.fetchone()
		return result_set[0] if result_set else 0

	def destroy(self):
		self._conn.close()
