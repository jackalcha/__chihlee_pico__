import time
from machine import Pin
led = Pin("LED",Pin.OUT)

while True:
    led.on()
    time.sleep_ms(300)
    led.off()
    time.sleep_ms(300)
    
    