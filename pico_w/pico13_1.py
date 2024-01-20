from machine import Pin
import time
red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)

while True:
    print(btn.value())
    time.sleep_ms(500)
    if btn.value() == 1 :
        red_led(1)
    else:
        red_led(0)
    
    