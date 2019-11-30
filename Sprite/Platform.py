"""
Class for the platforms of the game itself. Put in a separate module for potential future use.
"""
import os
# Imports to enable proper interaction regardless of regular module use.
from random import *
from Options.Settings import *
import pygame

vector = pygame.math.Vector2
white_box = (255, 255, 255)
asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.
candy_images = ['img/star_orange.png', 'img/star_purple.png', 'img/star_red.png', 'img/star_teal.png', 'img'
                                                                                                       '/star_white.png',
                'img/star_yellow.png', ]


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_folder, "Platform Tile Grass.png"))
        self.image = pygame.transform.scale(self.image, (120, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Candy(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self._layer = 0
        self.image = pygame.image.load(candy_images[randint(0, 5)])
        self.rect = self.image.get_rect()
        self.rect.x = randrange(window_width - self.rect.width)
        self.rect.y = randrange(-300, -55)
        self.game = game
        scale = randrange(50, 101) / 100
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale),
                                                         int(self.rect.height * scale)))

    def update(self):
        if self.rect.y > window_height:
            self.kill()
