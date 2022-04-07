import signal
import time
import sys

from pirc522 import RFID

run = True
rdr = RFID()

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        tag_hex = "".join(["%0.2X" % c for c in uid[0:4]])
        print("Card read UID: %s" % tag_hex)
        time.sleep(1)
