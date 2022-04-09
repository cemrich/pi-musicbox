#!/usr/bin/env python3

import mapping
from playerControl import PlayerControl
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

def on_tag_changed(tag_hex):
	if tag_hex:
		print("Tag detected: %s" % tag_hex)
		player.play(tag_hex)
	else:
		print("Tag removed")
		player.stop()

def main():
	global player
	player = mapping.MappedPlayer()
	#playerControl = PlayerControl(player)
	reader = rfid.Reader()
	reader.on_tag_changed(on_tag_changed)
	#player.play("start.mp3")

	try:
		print("Start detecting tags...")
		reader.start()
		reader.join()
	except KeyboardInterrupt:
		# if user hits Ctrl-C, exit gracefully
		pass

	player.destroy()
	reader.destroy()
	return 0

if __name__ == '__main__':
	sys.exit(main())
