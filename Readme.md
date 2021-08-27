# Pi Music Box

This project contains python3 scripts for a simple rfid controlled music box running on a raspberry pi zero.

## Setup

### Basic Pi Setup

You might want to set up the pi zero with [Raspberry Pi OS](https://www.raspberrypi.org/software/) Lite as a headless system to avoid the overhead of graphical output. There are good tutorials out there on how to set up a headless system, enable ssh and wifi before first boot (search for `wpa_supplicant`) and use `raspi-config`. 

If you do not (yet) feel comfortable without a graphical interface, go ahead and use the full Raspberry Pi OS image (with desktop) first.

### Software / Python

You have to have python3 and pip up and running on your system. Try `python3 --version` on your command line. If you don't get any version information install python3 with these command:

```
sudo apt update
sudo apt install python3 python3-pip
```

### Audio

This project uses a [Pimoroni Speaker pHAT](https://shop.pimoroni.com/products/speaker-phat) which replaces the pi zeros hdmi sound output. Setup instructions can be found at https://github.com/pimoroni/speaker-phat. It should be fine to replace the pHAT with any other audio solution, as long as the `audio-test.py` script produces sound.

### RFID

### Player Controls

## Hardware Components

### Raspberry Pi Zero W

- pinout: https://pinout.xyz/

### RC522 RFID card reader

- wiring: https://github.com/MiczFlor/RPi-Jukebox-RFID/wiki/Wiring_for_RC522_card_reader

### Pimoroni Speaker pHAT

- pinout: https://pinout.xyz/pinout/speaker_phat
- software / setup: https://github.com/pimoroni/speaker-phat

### MPR121 touch sensor

- short readme: https://github.com/quantenschaum/piripherals/blob/master/piripherals/mpr121.py
- datasheet: https://www.sparkfun.com/datasheets/Components/MPR121.pdf

## Similar Projects

- [Phoniebox: the RPi-Jukebox-RFID](https://github.com/MiczFlor/RPi-Jukebox-RFID)
- [Mopidy](https://mopidy.com/)

## Test Scripts
