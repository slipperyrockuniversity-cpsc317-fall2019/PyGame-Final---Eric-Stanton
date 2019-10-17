# Initial Imports for the pyGame Module
import pygame as game
import os
from Options.Settings import *

vector = game.math.Vector2  # Main vector for friction and movement physics.

asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.

# creating locations for sprite objects inside the grouping.
sprite_objects = game.sprite.Group()


# Original player class definition being initialized
class Player(game.sprite.Sprite):
    # Defining self attributes for coordinates, physics, etc.
    def __init__(self, instance):
        game.sprite.Sprite.__init__(self)  # Calling it's super class for proper function.
        self.image = game.image.load(os.path.join(image_folder, "Platformer_Sprite_1.png"))  # The picture of the
        # sprite itself. Os.Path to platform image.
        self.rect = self.image.get_rect()  # The boundry box "hitbox" of the player created. Start at center of screen
        self.rect.center = (window_width / 2, window_height / 2)
        self.position = vector(window_width / 2, window_height / 2)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)
        self.instance = instance  # Self-Reference to the game option and variables.

    def update(self):  # pygame movement for x and y co-ord. Now added key presses
        self.acceleration = vector(0, 0.5)  # Y acceleration to simulate gravity value for jumping.
        key_board = game.key.get_pressed()
        if key_board[game.K_LEFT]:
            self.acceleration.x = -starting_acceleration
        if key_board[game.K_RIGHT]:
            self.acceleration.x = starting_acceleration

        # Gaming Laws of motion for Velocity, Friction and sliding for smoother movement.
        self.acceleration.x += self.velocity.x * friction_level  # Creates "skidding" effect for realistic movement.
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration  # Motion equation to build up momentum when moving.

        self.rect.midbottom = self.position  # Puts center of Player class as same area as movement position.

        # If check to allow for proper wrapping around the screen if the x position is off the screen bounds.
        if self.position.x > window_width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = window_width

    def Jump(self):
        # Check to perform a single jump, reliant on platforms
        self.rect.x += 1
        touching = game.sprite.spritecollide(self, self.instance.platforms, False)
        self.rect.x -= 1
        if touching:
            self.velocity.y = -12
