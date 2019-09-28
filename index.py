# Initial Imports for the pyGame Module
import pygame

# Setup for the Height and Width of the window for the executable display


window_width = 500
window_height = 500
game_speed = 60  # ticks per second = frames per second

# pyGame Initialization (Music, Screen, Title, Timer Function)

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Plat-Man')
timer = pygame.time.Clock()
GREEN_BOX = (0, 255, 0)


# Original player class definition being initialized
class Player(pygame.sprite.Sprite):
    # Defining self attributes for coordinates, physics, etc.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Calling it's super class for proper function.
        self.image = pygame.Surface((25, 25))  # The picture of the sprite itself. Placeholder to be a green box.
        self.rect = self.image.get_rect()  # The boundry box "hitbox" of the player created. Start at center of screen
        self.rect.center = (window_width / 2, window_height / 2)
        self.image.fill(GREEN_BOX)

    def update(self):  # pygame movement for x and y co-ord, test will change for key presses in the future.
        self.rect.x = self.rect.x + 5
        if self.rect.left > window_width:
            self.rect.right = 0


# Creating a variable to contain all Sprite Objects from separate sprite modules, creating the imported player from mod.
sprite_objects = pygame.sprite.Group()
player = Player()
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
