# Setup for the main settings of the window for the executable display and the resulting files.
import random

window_width = 400
window_height = 650
game_speed = 75  # ticks per second = frames per second
game_title = "Plat-Man"  # Name of the game.
game_font = 'Serif'

'''
Previous Settings - Window
Next Settings - Properties called by the player (Friction Coefficient, Starting Acceleration etc.)
'''

starting_acceleration = 0.45
friction_level = -0.10

# Platform array list for easy spawning of platforms in the future.
# Uses random int for a few platforms from previous main.py file

random_width = random.randrange(75, 100)  # Range of width values to use for platform generation
random_height = random.randrange(0, 20)  # Range of random heights for beginner platform generation.

platform_array = [(0, window_height - 35, window_width + 50, 35), (window_width / 2 - 50, window_height * 0.75, 85, 20),
                  (window_width / 2 - 25, window_height * 0.50, 100, 100),
                  (random.randrange(0, window_width - random_width),
                   random.randrange(-50, -25), random_width, 25), (random.randrange(0, window_width - random_width),
                                                                   random.randrange(-40, -25), random_width, 25),
                  (200, 200, random_width, random_height)]

'''
Color Variables for random text or BG drawing.
'''

White = (155, 155, 155)

Black = (0, 0, 0)

Red = (203, 0, 0)

Orange = (255, 116, 21)
