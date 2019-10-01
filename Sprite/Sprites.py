# Initial Imports for the pyGame Module
import pygame
import os

# Window values to stop circular import error.
window_height = 500
window_width = 500

asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.


# Original player class definition being initialized
class Player(pygame.sprite.Sprite):
    # Defining self attributes for coordinates, physics, etc.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Calling it's super class for proper function.
        self.image = pygame.image.load(os.path.join(image_folder, "Platformer_Sprite_1.png"))  # The picture of the
        # sprite itself. Os.Path to platform image.
        self.rect = self.image.get_rect()  # The boundry box "hitbox" of the player created. Start at center of screen
        self.rect.center = (window_width / 2, window_height / 2)

    def update(self):  # pygame movement for x and y co-ord, test will change for key presses in the future.
        self.rect.x = self.rect.x + 5
        if self.rect.left > window_width:
            self.rect.right = 0
