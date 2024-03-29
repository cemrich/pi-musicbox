# Pi Music Box

This project contains python3 scripts for a simple rfid controlled music box running on a raspberry pi zero.

## Setup

### Basic Pi Setup

You might want to set up the pi zero with [Raspberry Pi OS](https://www.raspberrypi.org/software/) Lite as a headless system to avoid the overhead of graphical output. There are good tutorials out there on how to set up a headless system, enable ssh and wifi before first boot. I used the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) for easy setup.

If you do not (yet) feel comfortable without a graphical interface, go ahead and use the full Raspberry Pi OS image (with desktop) first.

### Software / Python / VLC

You have to have python3 and pip up and running on your system. Try `python3 --version` on your command line. If you don't get any version information install python3 with these command:

```
sudo apt update
sudo apt install python3 python3-pip
```

Also, you need VLC installed for playback:

```
sudo apt-get install vlc
```

### Audio

This project uses a [Pimoroni Speaker pHAT](https://shop.pimoroni.com/products/speaker-phat) which replaces the pi zeros hdmi sound output. Setup instructions can be found at https://github.com/pimoroni/speaker-phat. It should be fine to replace the pHAT with any other audio solution, as long as the `audio-test.py` script produces sound.

To get vlc not to spill error messages, you also need to install pulseaudio:

    sudo apt-get install pulseaudio

### RFID

After wiring the RC522 rfid card reader you have to enable the spi interface.

    sudo raspi-config

Select "Interface Options" > "SPI" > "Yes".

Run `src/test-scripts/rfid-test.py` to test the reader.

### Player Controls

To control the player (skipping, volume, etc.) this project uses a MPR121 touch sensor. Because the default i2c pins are already taken by the Speaker pHAT (and I want to avoid soldering at this point), we create an [additional i2c bus](https://www.instructables.com/Raspberry-PI-Multiple-I2c-Devices/) on some available pins.

- Open the confog file with `sudo nano /boot/config.txt`
- Add the line `dtoverlay=i2c-gpio,bus=4,i2c_gpio_delay_us=1,i2c_gpio_sda=17,i2c_gpio_scl=27` and save. This line will create an aditional i2c bus (bus 4) on GPIO 17 as SDA and GPIO 27 as SCL. Reboot for this change to take effect.

- Connect your the pins of your MPR121 touch sensor to the pi:
  - SDA: GPIO17
  - SCL: GPIO27
  - IRQ: GPIO0
  - ground: use any [fitting pin](https://pinout.xyz/pinout/ground#)
  - 3.3V: pin 1 ([the other one](https://pinout.xyz/pinout/3v3_power#) is occupied by the rfid module)

- Run `sudo apt install -y i2c-tools` to install some utilities to detect i2c devices. Run `sudo i2cdetect -y 4`. You should see output with the sensors address `5A` somewhere in it. If you get an error message or no address check your wiring and boot config.

- Run `python3 src/tests-scripts/touch-test.py`. It should produce an output if you touch any pin on the sensor.

### Player Code Setup with systemd

```
sudo git clone https://github.com/cemrich/pi-musicbox/ /opt/musicbox
sudo chown pi:pi -R /opt/musicbox
cd /opt/musicbox
pip3 install -r requirements.txt
sudo cp tools/musicbox.service /usr/lib/systemd/user/
```

Allowing the pi user to start scripts on boot without login:

    loginctl enable-linger pi

Finds the new service file:

    systemctl --user daemon-reload

Enables it for start at boot time:

    systemctl --user enable musicbox

Controlling the service:

```
systemctl --user status musicbox
systemctl --user stop musicbox
systemctl --user start musicbox
systemctl --user restart musicbox
```

Reading the log output:

    journalctl --user -u musicbox -f 

## Expose Samba Share

To access files on our musicbox we will expose them as samba share over network:

```
sudo apt-get install samba samba-common-bin
sudo nano /etc/samba/smb.conf
```

Add following lines to the file:

```
[files]
path = /opt/musicbox/files
writeable=Yes
create mask=0777
directory mask=0777
public=no
```

Now we need to create a new samba user. Here the user is named "pi":

```
sudo smbpasswd -a pi
```

After restarting samba we can connect from another machine to \\<my-pi-ip-or-network-name>\files:

```
sudo systemctl restart smbd
```

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
