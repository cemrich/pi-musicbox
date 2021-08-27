"""
Tests if the MPR121 touch sensor is set up correctly.
See readme for set up instructions.
"""

from piripherals import MPR121

mpr = MPR121(bus=4)

for i in range(12):
	# print status on touch and release
    mpr.on_touch(i, lambda *x: print(f'pin {x[1]} is {"pressed" if x[0] else "released"}'))

input("Touch a pin to generate output. Press Enter stop...")
