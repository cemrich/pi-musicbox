#!/usr/bin/env python3

import mapping
import rfid
import sys
import time

SLEEPTIME_SECONDS = 0.1

def on_loop_iteration(reader, player):
	try:
		if reader.has_hex_changed():
			if reader.tag_hex:
				print("Tag detected: %s" % reader.tag_hex)
				player.play(reader.tag_hex)
			else:
				print("Tag removed")
				player.stop()
	except IOError as exc:
		print("-IOError: %s" % exc)

def start_main_loop(reader, player):
	global SLEEPTIME_SECONDS

	while True:
		on_loop_iteration(reader, player)
		time.sleep(SLEEPTIME_SECONDS)

def main():
	player = mapping.MappedPlayer()
	reader = rfid.Reader()

	try:
		print("Start detecting tags...")
		start_main_loop(reader, player)
	except KeyboardInterrupt:
		# if user hits Ctrl-C, exit gracefully
		pass

	player.destroy()
	reader.destroy()
	return 0

if __name__ == '__main__':
	sys.exit(main())
