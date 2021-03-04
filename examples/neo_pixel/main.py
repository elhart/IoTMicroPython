from machine import Pin
from neopixel import NeoPixel

pin = 4
n_led = 8

np = NeoPixel(Pin(pin), n_led)

np[0] = (64, 0, 0)     # set to red, quarter brightness
np[1] = (0, 64, 0)     # set to green, quarter brightness
np[2] = (0, 0, 64)     # set to blue, quarter brightness

np.write()
