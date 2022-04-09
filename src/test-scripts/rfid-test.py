import signal
import time
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import rfid

reader = rfid.Reader()

def end_read(signal, frame):
	print("\nCtrl+C captured, ending read.")
	reader.destroy()
	sys.exit()

signal.signal(signal.SIGINT, end_read)


print("Starting")

while True:
	if reader.has_hex_changed():
		if reader.tag_hex:
			print("Tag detected: %s" % reader.tag_hex)
		else:
			print("Tag removed")

		time.sleep(0.1)
