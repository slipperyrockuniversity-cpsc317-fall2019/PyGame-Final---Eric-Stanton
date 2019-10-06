import pygame as game
import os
from Sprite.Sprites import Player, sprite_objects
from Options.Settings import *
from Sprite.Platform import *


# Creating class of game to properly initialize
class Game:
    def __init__(self):
        # Game Start screen
        # pyGame Initialization (Music, Screen, Title, Timer Function)
        self.alive = True
        game.init()
        game.mixer.init()
        self.window = game.display.set_mode((window_width, window_height))
        game.display.set_caption(game_title)
        self.timer = game.time.Clock()

    def begin(self):
        # game creation function.
        self.platforms = game.sprite.Group()
        player = Player()
        sprite_objects.add(player)
        platform_1 = Platform(0, window_height - 40, window_width, 40)
        sprite_objects.add(platform_1)
        self.platforms.add(platform_1)
        self.active()

    def active(self):
        # Loop of the game itself, uses other defined functions.
        self.on = True
        while self.on:
            self.timer.tick(game_speed)
            self.event_handles()
            self.update()
            self.draw()

    def update(self):
        # Update draw of the game
        sprite_objects.update()

    def event_handles(self):
        for key in game.event.get():
            if key.type == game.QUIT:
                if self.on:
                    self.on = False
            self.alive = False

    def draw(self):
        # Game loop which draws the main graphics
        self.window.fill((0, 0, 0))
        sprite_objects.draw(self.window)
        # Create flip display to re-draw elements
        game.display.flip()

    def make_ending_screen(self):
        # You died screen.
        pass

    def startup_screen(self):
        # Screen when first turned on.
        pass


win = Game()
win.make_ending_screen()
while win.alive:
    win.begin()
    win.startup_screen()

game.quit()
