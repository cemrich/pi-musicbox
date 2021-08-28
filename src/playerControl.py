from piripherals import MPR121

class PlayerControl:

	CHANNEL_NEXT = 0
	CHANNEL_PREV = 3

	def __init__(self, player):
		self._player = player
		mpr = MPR121(bus=4, irq=0)

		mpr.on_touch(self.CHANNEL_NEXT, self._onNext)
		mpr.on_touch(self.CHANNEL_PREV, self._onPrev)

	def _onNext(self, isPressed, pinNumber):
		if isPressed:
			print("next touch button pressed")
			self._player.next()

	def _onPrev(self, isPressed, pinNumber):
		if isPressed:
			print("prev touch button pressed")
			self._player.prev()
