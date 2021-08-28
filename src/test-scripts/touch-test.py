"""
Tests if the MPR121 touch sensor is set up correctly.
See readme for set up instructions.
"""

from piripherals import MPR121

mpr = MPR121(bus=4, irq=0)

def _onTouch(isPressed, pinNumber):
	pressedMessage = "pressed" if isPressed else "released"
	print('pin %d is %s' % (pinNumber, pressedMessage))

for i in range(12):
	# print status on touch and release
    mpr.on_touch(i, _onTouch)

input("Touch a pin to generate output. Press Enter stop...")
