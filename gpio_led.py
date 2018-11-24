from gpiozero import LED
from time import sleep

led = LED(3)
 
while True:
    for I in range(0,4):
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)
    for I in range(0,4):
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
    for I in range(0,4):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    for I in range(0,4):
        led.on()
        sleep(0.4)
        led.off()
        sleep(0.4)


