from pirc522 import RFID

class Reader:

	def __init__(self):
		self.rdr = RFID()
		self.tagHex = None

	def hasHexChanged(self):
		newTagHex = None
		(error, data) = self.rdr.request()

		if not error:
			(error, uid) = self.rdr.anticoll()

			if error:
				raise "Could not read tag id: %s" % error
			else:
				newTagHex = "".join(["%0.2X" % c for c in uid[0:4]])

		# workaround for bug https://github.com/ondryaso/pi-rc522/issues/10
		self.rdr.halt()

		hasChanged = newTagHex != self.tagHex
		self.tagHex = newTagHex
		return hasChanged

	def destroy(self):
		self.rdr.cleanup()
