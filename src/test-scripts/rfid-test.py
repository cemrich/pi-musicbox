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

def on_tag_changed(tag_hex):
	print("on_tag_changed callback: %s" % tag_hex)

reader.on_tag_changed(on_tag_changed)
signal.signal(signal.SIGINT, end_read)


print("Start detecting tags...")

reader.start()
reader.join()
