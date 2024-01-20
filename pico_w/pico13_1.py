from machine import Pin
import time
red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False

while True:
    if btn.value():
        is_press = True
        red_led(1)
    elif is_press :
        print('release')
        is_press = False
        red_led(0)
    
    