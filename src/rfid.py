#!/usr/bin/env python3

import signal
import time
import mapping
import pygame
import sys

from pirc522 import RFID

rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
	print("\nCtrl+C captured, ending read.")
	rdr.cleanup()
	sys.exit()

def main():
	signal.signal(signal.SIGINT, end_read)

	try:
		player = mapping.MappedPlayer()
	except pygame.error as exc:
		print("Could not initialize sound system: %s" % exc)
		return 1

	print("Starting...")
	while True:
		(error, data) = rdr.request()

		if error:
			# TODO: stop player
			print("No tag detected: %s" % error)
		else:
			(error, uid) = rdr.anticoll()

			if error:
				print("Could not read tag id: %s" % error)
			else:
				hexString = "".join(["%0.2X" % c for c in uid[0:4]])
				print("Tag detected: %s" % hexString)
				player.play(hexString)

		time.sleep(1)

if __name__ == '__main__':
	sys.exit(main())
