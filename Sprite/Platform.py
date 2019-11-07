"""
Class for the platforms of the game itself. Put in a separate module for potential future use.
"""
# Imports to enable proper interaction regardless of regular module use.

import pygame
from Options.Settings import *
import os

vector = pygame.math.Vector2
white_box = (255, 255, 255)
asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "Platform Tile Grass.png"))
        self.image = pygame.transform.scale(self.image, (120, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
