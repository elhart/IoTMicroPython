from machine import Pin
from time import sleep

# both esp8266 and esp32 have led on pin 2
led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(1)
