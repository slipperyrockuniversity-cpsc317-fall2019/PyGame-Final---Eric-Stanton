"""
Class for the platforms of the game itself. Put in a separate module for potential future use.
"""
# Imports to enable proper interaction regardless of regular module use.

import pygame
from Options.Settings import *

vector = pygame.math.Vector2
white_box = (255, 255, 255)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(white_box)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
