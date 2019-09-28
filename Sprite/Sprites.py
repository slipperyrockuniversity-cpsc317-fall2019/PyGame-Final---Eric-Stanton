# Initial Imports for the pyGame Module

import pygame

import random

from pygame import *


# Class player sprite creation for import into main game file

class Player(pygame.sprite.Sprite):
    # Defining self attributes for coordinates, physics, etc.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Calling it's super class for proper function.
        self.image = pygame.Surface((25, 25))  # The picture of the sprite itself. Placeholder to be a green box.
        self.rect = self.image.get_rect()  # The boundry box "hitbox" of the player created. Start at center of screen
        self.rect.center = (window_width / 2, window_height / 2)
        self.image.fill(lime)
