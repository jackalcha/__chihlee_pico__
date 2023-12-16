import time
from machine import Pin
led = Pin("LED",Pin.OUT)

while True:
    led.high()
    time.sleep_ms(100)
    led.low()
    time.sleep_ms(100)
    
    
    