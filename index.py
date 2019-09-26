# Initial Imports for the pyGame Module

import pygame

import random

from pygame import *

# Setup for the Height and Width of the window for the executable display

window_width = 500
window_height = 500
game_speed = 30

# pyGame Initialization (Music, Screen, Title, Timer Function)

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Plat-Man')
timer = pygame.time.Clock()

# Main loop for game drawing function, event handling, listening,
# set active to false to end game after ending condition met.

active = True
while active:
    # Make the game run at the specified speed of the game - Avoid Lag from different elements.
    timer.tick(game_speed)
    # To Do: Create Graphics to draw in background of window file.
    # light blue screen of death used for screen placeholder until replacement found.
    window.fill((0, 255, 255))
    # Create flip display to re-draw elements
    pygame.display.flip()
    # Input or Key Pressing Event Statements to Exit, Move, Etc.
    # Formulaic Loop to check for any relevant keys (2d Platform = up down left right jump)
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            active = False  # Quit game if X button is pressed.

pygame.quit()  # Automatically end the game loop.
