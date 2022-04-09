import threading
from pirc522 import RFID

SLEEPTIME_SECONDS = 1

class Reader(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

		self._rdr = RFID()
		self._tag_hex = None
		self._stop_event = threading.Event()
		self._on_tag_changed_callback = None

	def on_tag_changed(self, callback):
		self._on_tag_changed_callback = callback

	def run(self):
		self._running = True

		while not self._stop_event.is_set():

			if self._tag_hex == None:
				# Wait blocking for any tag when previously no one was present.
				# This allows for low cpu usage
				self._rdr.wait_for_tag()
			else:
				# We do not want to block this loop when user removes a rfid card.
				# Instead we want to detect removed rfid cards as "None".
				# As self._rdr.wait_for_tag() has no timeout, we use simple polling.
				self._stop_event.wait(SLEEPTIME_SECONDS)

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

			has_changed = new_tag_hex != self._tag_hex

			if has_changed:
				# print("Tag detected: %s" % new_tag_hex)

				if self._on_tag_changed_callback:
					self._on_tag_changed_callback(new_tag_hex)

			self._tag_hex = new_tag_hex

		print("Shutting down down rfid reader...")
		self._rdr.cleanup()

	def destroy(self):
		# ending main loop in run method
		self._stop_event.set()

		# hack to return from self._rdr.wait_for_tag()
		self._rdr.irq_callback(None)
