#!/usr/bin/env python3

import mapping
import rfid
import sys
import time

SLEEPTIME_SECONDS = 0.1

def onLoopIteration(reader, player):
	try:
		if reader.hasHexChanged():
			if reader.tagHex:
				print("Tag detected: %s" % reader.tagHex)
				player.play(reader.tagHex)
			else:
				print("Tag removed")
				player.stop()
	except IOError as exc:
		print("%s" % exc)

def startMainLoop(reader, player):
	global SLEEPTIME_SECONDS

	while True:
		onLoopIteration(reader, player)
		time.sleep(SLEEPTIME_SECONDS)

def main():
	player = mapping.MappedPlayer()
	reader = rfid.Reader()
	player.setVolume(0.5)

	try:
		print("Start detecting tags...")
		startMainLoop(reader, player)
	except KeyboardInterrupt:
		# if user hits Ctrl-C, exit gracefully
		pass

	reader.destroy()
	return 0

if __name__ == '__main__':
	sys.exit(main())
