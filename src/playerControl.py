import math
from piripherals import MPR121

class PlayerControl:

	CHANNEL_NEXT = 0
	CHANNEL_PREV = 3
	CHANNEL_VOLUME_LOW = 11
	CHANNEL_VOLUME_HIGH = 4

	MIN_VOLUME = 30
	MAX_VOLUME = 100

	def __init__(self, player):
		self._player = player
		mpr = MPR121(bus=4, irq=0)

		mpr.on_touch(self.CHANNEL_NEXT, self._onNext)
		mpr.on_touch(self.CHANNEL_PREV, self._onPrev)

		volume_direction = int(math.copysign(1, self.CHANNEL_VOLUME_HIGH - self.CHANNEL_VOLUME_LOW))
		print("volume_direction: %d" % volume_direction)

		for i in range(self.CHANNEL_VOLUME_LOW, self.CHANNEL_VOLUME_HIGH + volume_direction, volume_direction):
			print("register volume touch button: %d" % i)
			mpr.on_touch(i, self._onVolume)

	def _onNext(self, isPressed, pinNumber):
		if isPressed:
			print("next touch button pressed")
			self._player.next()

	def _onPrev(self, isPressed, pinNumber):
		if isPressed:
			print("prev touch button pressed")
			self._player.prev()

	def _onVolume(self, isPressed, pinNumber):
		if isPressed:
			volume = int(self._mapFromTo(pinNumber, self.CHANNEL_VOLUME_LOW, self.CHANNEL_VOLUME_HIGH, self.MIN_VOLUME, self.MAX_VOLUME))

			print("volume touch button pressed: %d - set volume to: %d" % (pinNumber, volume))
			self._player.set_volume(volume)

	def _mapFromTo(self, value, fromInput, toInput, fromOutput, toOutput):
		y = (value-fromInput) / (toInput-fromInput) * (toOutput-fromOutput) + fromOutput
		return y
