from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN)

def change_led(button):
    led.value(not led.value())

button.irq(trigger=Pin.IRQ_FALLING, handler=change_led)
