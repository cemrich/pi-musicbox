import pygame
import sys

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

class Player:

	def __init__(self):
		self.clock = pygame.time.Clock()

		pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)


	def play(self, filePath):
		"""Stream music with mixer.music module.

		This will stream the sound from disk while playing.
		"""

		pygame.mixer.music.load(filePath)
		pygame.mixer.music.play()

	def stop(self):
		pygame.mixer.music.stop()
