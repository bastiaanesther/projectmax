#|----------------------------------|
#| Code geschreven door:            |
#| Esther Bron en Bastiaan van Dam
#|----------------------------------|

# Import libraries:
from max import laat_led
import pygame
from gpiozero import LED

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
               
    laat_led.knipperen(led)
