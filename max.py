#|----------------------------------|
#| Code geschreven door:            |
#| Esther Bron en Bastiaan van Dam
#| Testje!
#|----------------------------------|

# Import libraries:
from max import led_strip
import pygame

# Led
from gpiozero import LED

#Led Strip
import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Led Strip: Configure the count of pixels:
PIXEL_COUNT = 30

# Led Strip: Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# variabelen:
done = False    # Variabelen voor stoppen while loop
 
# Progamma:
pygame.init()
pygame.display.set_mode()
while not done: # While loop stop als done true wordt (door Esc toets kyboard)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            done = True
               
    # Clear all the pixels to turn them off.
    pixels.clear()
    pixels.show()  # Make sure to call show() after changing any pixels!
    led_strip.rainbow_cycle(pixels, wait=0.02)
    led_strip.brightness_decrease(pixels)
