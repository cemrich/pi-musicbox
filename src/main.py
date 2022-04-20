#!/usr/bin/env python3

import mapping
from playerControl import PlayerControl
from sfxPlayer import SfxPlayer, Sfx
import rfid
import asyncio
import sys

SLEEPTIME_SECONDS = 0.1

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def on_tag_changed(tag_hex):
	if tag_hex:
		print("Tag detected: %s" % tag_hex)
		sfxPlayer.play(Sfx.TAG_DETECTED)
		loop.call_soon_threadsafe(lambda: player.play(tag_hex))
	else:
		print("Tag removed")
		sfxPlayer.play(Sfx.TAG_REMOVED)
		loop.call_soon_threadsafe(player.stop)

def main():
	global player, sfxPlayer

	sfxPlayer = SfxPlayer()
	player = mapping.MappedPlayer(sfxPlayer)

	playerControl = PlayerControl(player)
	reader = rfid.Reader()
	reader.on_tag_changed(on_tag_changed)

	sfxPlayer.play(Sfx.START)

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
