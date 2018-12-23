#|----------------------------------|
#| Code geschreven door:            |
#| Esther Bron en Bastiaan van Dam  |
#|----------------------------------|

# Import libraries:
import pygame
from gpiozero import LED
from time import sleep

# variabelen:
done = False    # Variabelen voor stoppen while loop
led = LED(3)
 
# Progamma:
pygame.init()
pygame.display.set_mode()
while not done: # While loop stop als done true wordt (door Esc toets kyboard)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            done = True
        
    led.on()
    sleep(0.05)
    led.off()
    sleep(0.05)

