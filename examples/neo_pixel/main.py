"""
Example how to use NeoPixel library to drive an array of LEDs
using esp8266 and esp32 development boards
"""

from time import sleep
from machine import Pin
from neopixel import NeoPixel

# on esp8266, pin 4 is labeled D2
# on esp32, pin 4 is D4
pin = 4
n_led = 8

np = NeoPixel(Pin(pin), n_led)

def rainbow():
    """
    Setting all 8 led to different colors
    """
    np[0] = (64, 0, 0)      # set to red
    np[1] = (64, 32, 0)     # set to orange
    np[2] = (64, 64, 0)     # set to yellow
    np[3] = (0, 64, 0)      # set to green
    np[4] = (0, 0, 64)      # set to blue
    np[5] = (38, 0, 64)
    np[6] = (38, 0, 52)
    np[7] = (0, 0, 24)
    np.write()

def clear():
    for pixel in range(0, n_led):
        np[pixel] = (0, 0, 0)

def spin():
    """
    A single pixel (lef) moving along the array
    """
    while True:
        for pixel in range(0, n_led):
            clear()
            np[pixel] = (64, 0, 0)
            np.write()
            sleep(0.3)

# spin()
rainbow()
