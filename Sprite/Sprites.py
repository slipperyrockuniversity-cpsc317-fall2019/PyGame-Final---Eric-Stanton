# Initial Imports for the pyGame Module
import pygame as game
import os
from Options.Settings import *

asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.

# creating locations for sprite objects inside the grouping.
sprite_objects = game.sprite.Group()


# Original player class definition being initialized
class Player(game.sprite.Sprite):
    # Defining self attributes for coordinates, physics, etc.
    def __init__(self):
        game.sprite.Sprite.__init__(self)  # Calling it's super class for proper function.
        self.image = game.image.load(os.path.join(image_folder, "Platformer_Sprite_1.png"))  # The picture of the
        # sprite itself. Os.Path to platform image.
        self.rect = self.image.get_rect()  # The boundry box "hitbox" of the player created. Start at center of screen
        self.rect.center = (window_width/2,window_height/2)
        self.vx = 0
        self.vy = 0

    def update(self):  # pygame movement for x and y co-ord. Now added key presses
        self.vx = 0
        key_board = game.key.get_pressed()
        if key_board[game.K_LEFT]:
            self.vx = -5
        if key_board[game.K_RIGHT]:
            self.vx = 5
        self.rect.x += self.vx  # If left or right keys pressed, left or right movement assured.
        self.rect.y += self.vy  # Future jump movement or gravity.
