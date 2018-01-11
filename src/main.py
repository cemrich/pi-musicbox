import player
import pygame
import sys
import os

def main():
	filesDir = os.path.dirname(os.path.abspath(__file__)) + "/../files/"

	try:
		musicPlayer = player.Player()
	except pygame.error as exc:
		print("Could not initialize sound system: %s" % exc)
		return 1

	try:
		try:
			musicPlayer.play(filesDir + "test.mp3")
			input("Press Enter to stop playback...")
			musicPlayer.stop()
			input("Press Enter to exit...")
		except pygame.error as exc:
			print("Could not play sound file: %s" % exc)
			print(exc)
	except KeyboardInterrupt:
		# if user hits Ctrl-C, exit gracefully
		pass
	return 0

if __name__ == '__main__':
	sys.exit(main())
