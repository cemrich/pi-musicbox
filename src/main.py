import mapping
import pygame
import sys

def main():
	try:
		player = mapping.MappedPlayer()
	except pygame.error as exc:
		print("Could not initialize sound system: %s" % exc)
		return 1

	try:
		try:
			soundId = input("Input sound id: ")
			player.play(soundId)
			input("Press Enter to stop...")
			player.stop()
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
