#!/usr/bin/env python3

import mapping
import rfid
import pygame
import sys
import time

SLEEPTIME_SECONDS = 0.1

def onLoopIteration(reader, player):
	if reader.hasHexChanged():
		if reader.tagHex:
			print("Tag detected: %s" % reader.tagHex)
			try:
				player.play(reader.tagHex)
			except pygame.error as exc:
				print("Could not play sound file: %s" % exc)
		else:
			print("Tag removed")
			player.stop()

def startMainLoop(reader, player):
	global SLEEPTIME_SECONDS

	while True:
		onLoopIteration(reader, player)
		time.sleep(SLEEPTIME_SECONDS)

def main():
	try:
		player = mapping.MappedPlayer()
	except pygame.error as exc:
		print("Could not initialize sound system: %s" % exc)
		return 1

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
