# Initial Imports for the pyGame Module
import pygame
import os
from Sprite import Sprites
from Options.Settings import *

# Creating folder to hold the assets for the game.
asset_folder = os.path.dirname(__file__)  # Universal function for multiple OS system
image_folder = os.path.join(asset_folder, 'img')  # Joining the future img folder with OS.Path.

# pyGame Initialization (Music, Screen, Title, Timer Function)

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Plat-Man')
timer = pygame.time.Clock()

# Creating a variable to contain all Sprite Objects from separate sprite modules, creating the imported player from mod.
sprite_objects = pygame.sprite.Group()
player = Sprites.Player()
sprite_objects.add(player)

# Main loop for game drawing function, event handling, listening,
# set active to false to end game after ending condition met.
active = True
while active:
    # Make the game run at the specified speed of the game - Avoid Lag from different elements.
    timer.tick(game_speed)
    # To Do: Create Graphics to draw in background of window file.
    # Update loop to redraw all sprites from previous grouping.
    sprite_objects.update()
    # Fill the screen with a Placeholder Color, and redraw the sprites to the game board.
    window.fill((0, 255, 255))
    sprite_objects.draw(window)
    # Create flip display to re-draw elements
    pygame.display.flip()
    # Input or Key Pressing Event Statements to Exit, Move, Etc.
    # Formulaic Loop to check for any relevant keys (2d Platform = up down left right jump)
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            active = False  # Quit game if X button is pressed.

pygame.quit()  # Automatically end the game loop.
