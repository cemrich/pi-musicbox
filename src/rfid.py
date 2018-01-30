from pirc522 import RFID

class Reader:

	def __init__(self):
		self._rdr = RFID()
		self.tag_hex = None

	def has_hex_changed(self):
		new_tag_hex = None
		(error, data) = self._rdr.request()

		if not error:
			(error, uid) = self._rdr.anticoll()

			if error:
				raise IOError("Could not read tag id: %s" % error)
			else:
				new_tag_hex = "".join(["%0.2X" % c for c in uid[0:4]])

		# workaround for bug https://github.com/ondryaso/pi-rc522/issues/10
		self._rdr.halt()

		has_changed = new_tag_hex != self.tag_hex
		self.tag_hex = new_tag_hex
		return has_changed

	def destroy(self):
		self._rdr.cleanup()
