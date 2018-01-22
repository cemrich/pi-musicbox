import pygame
import sys
import os
import time
import threading

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

class Player:

	def __init__(self):
		self.clock = pygame.time.Clock()
		self.shouldPlay = False
		self.volume = 1.0

		pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)

	def setVolume(self, volume):
		self.volume = volume
		pygame.mixer.music.set_volume(self.volume)

	def play(self, filePath):
		"""Stream music with mixer.music module.

		This will stream the sound from disk while playing.
		"""

		self.shouldPlay = True

		if os.path.isdir(filePath):
			allFiles = [os.path.join(filePath, f) for f in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, f))]

			thread = threading.Thread(target=self._playMultiple, args=([allFiles]))
			thread.daemon = True # Daemonize thread
			thread.start()
		else:
			thread = threading.Thread(target=self._playSingle, args=([filePath]))
			thread.daemon = True # Daemonize thread
			thread.start()
			self._playSingle(filePath)


	def stop(self):
		self.shouldPlay = False
		thread = threading.Thread(target=self._fadeOut)
		thread.daemon = True # Daemonize thread
		thread.start()

	def _fadeOut(self):
		pygame.mixer.music.fadeout(1000)

	def _playMultiple(self, allFiles):
		for audioFile in allFiles:
			if self.shouldPlay:
				self._playSingle(audioFile)
				while pygame.mixer.music.get_busy():
					time.sleep(0.1)

	def _playSingle(self, filePath):
		pygame.mixer.music.load(filePath)
		pygame.mixer.music.set_volume(self.volume)
		pygame.mixer.music.play()
