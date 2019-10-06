# Setup for the main settings of the window for the executable display and the resulting files.
window_width = 400
window_height = 400
game_speed = 60  # ticks per second = frames per second
game_title = "Plat-Man"  # Name of the game.

'''
Previous Settings - Window
Next Settings - Properties called by the player (Friction Coefficient, Starting Acceleration etc.)
'''

starting_acceleration = 0.5
friction_level = -0.20

# Platform array list for easy spawning of platforms in the future.
platform_array = [(0, window_height - 40, window_width, 40), (window_width / 2 - 50, window_height * 0.75, 120, 20),
                  (30, 62, 24, 58), (120, 200, 88, 40), (100, 120, 60, 45)]
