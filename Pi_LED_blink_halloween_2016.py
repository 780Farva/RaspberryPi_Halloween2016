# script to blink LED's two at a time for Bryce and Naz's bush outside during halloween

import time
import random
import pins


class BushEyes:
    pin = 0

    def __init__(self, pin):
        self.pin = pin


# Use the following GPIOs for LEDs
eyesList = [BushEyes(2),
            BushEyes(3),
            BushEyes(4),
            BushEyes(24),
            BushEyes(25),
            BushEyes(7),
            BushEyes(8),
            BushEyes(9),
            BushEyes(10),
            BushEyes(11),
            BushEyes(14),
            BushEyes(15),
            BushEyes(17),
            BushEyes(18),
            BushEyes(27)]

# Create a pin manager to help us write pin values and directions
pinMgr = pins.PinManager()

for eyes in eyesList:
    pinMgr.unexport_pin(eyes.pin)
    pinMgr.export_pin(eyes.pin)
    pinMgr.define_direction(eyes.pin, 'out')

random = random.Random()


def getEyesToBlink():
    eyes_to_blink = []

    for i in range(3):
        index = random.randint(0, len(eyesList) - 1)
        eyes_to_blink.append(eyesList[index])

    return eyes_to_blink


while 1:
    eyesToBlink = getEyesToBlink()

    for selectedEye in eyesToBlink:
        pinMgr.set_pin_value(selectedEye.pin, 1)
    time.sleep(1)

    for selectedEye in eyesToBlink:
        pinMgr.set_pin_value(selectedEye.pin, 0)
    time.sleep(0.5)

for eyes in eyesList:
    pinMgr.unexport_pin(eyes.pin)
