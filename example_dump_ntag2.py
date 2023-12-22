"""
This example shows connecting to the PN532 and reading an NTAG215
type RFID tag
"""

import RPi.GPIO as GPIO
from pn532 import *

pn532 = PN532_SPI(cs=4, reset=20, debug=False)
#pn532 = PN532_I2C(debug=False, reset=20, req=16)
#pn532 = PN532_UART(debug=False, reset=20)

ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with NTAG215 cards
pn532.SAM_configuration()

print('Waiting for RFID/NFC card to read from!')
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    print('.', end="")
    # Try again if no card is available.
    if uid is not None:
        break
print('Found card with UID:', [hex(i) for i in uid])

# Now we try to go through 5 pages of 4 bytes per page.
for i in range(5):
    try:
        print(i, ':', ' '.join(['%02X' % x
            for x in pn532.ntag2xx_read_block(i)]))
    except pn532.PN532Error as e:
        print(e.errmsg)
        break
GPIO.cleanup()
