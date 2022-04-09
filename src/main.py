#!/usr/bin/env python3

import mapping
from playerControl import PlayerControl
import rfid
import asyncio
import sys
import time

SLEEPTIME_SECONDS = 0.1

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def on_tag_changed(tag_hex):
	if tag_hex:
		print("Tag detected: %s" % tag_hex)
		loop.call_soon_threadsafe(lambda: player.play(tag_hex))
	else:
		print("Tag removed")
		loop.call_soon_threadsafe(player.stop)

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
		loop.run_forever()
	except KeyboardInterrupt:
		# if user hits Ctrl-C, exit gracefully
		pass

	print("Shutting down musicbox main program...")
	loop.close()
	player.destroy()
	reader.destroy()
	return 0

if __name__ == '__main__':
	sys.exit(main())
