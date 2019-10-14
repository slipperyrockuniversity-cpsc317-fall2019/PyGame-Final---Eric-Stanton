import pygame as game
import random
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
        self.player = Player(self)

    def begin(self):
        # Game creation function, platform creation function.
        self.platforms = game.sprite.Group()
        sprite_objects.add(self.player)
        for select in platform_array:
            plat = Platform(*select)  # Use explosion of array to select random platform generators.
            sprite_objects.add(plat)
            self.platforms.add(plat)  # Add the resulting platform array to the game
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
        # Collision check for platforms - Enable jumping through platforms.
        if self.player.velocity.y > 0:
            touching = game.sprite.spritecollide(self.player, self.platforms, False)
            if touching:
                self.player.position.y = touching[0].rect.top  # If player touches platform, force position on top.
                self.player.velocity.y = 0  # Stop falling, lack of this line causes quicksand effect.
        # Check for the scrolling window for upward movement.
        if self.player.rect.top <= window_height / 4:
            self.player.position.y += abs(self.player.velocity.y)  # Force the y position upwards by the Vel. setting
            for select in self.platforms:
                select.rect.y += abs(self.player.velocity.y)  # Drag the platforms along with the Player.
                if select.rect.top >= window_height:
                    select.kill()  # If the platforms goes below the window height, kill the object.

        # Spawn brand new platforms from random number values. Keep an average number of them.
        while len(self.platforms) < 7:
            spawn = Platform(random.randrange(0, window_width - random_width),
                             random.randrange(-50, -35),random_width, 25)  # Random x and y values called
            # width and height sanity checks
            self.platforms.add(spawn)
            sprite_objects.add(spawn)

    def event_handles(self):
        for key in game.event.get():
            if key.type == game.QUIT:
                if self.on:
                    self.on = False
            self.alive = False
            if key.type == game.KEYDOWN:
                if key.key == game.K_SPACE:
                    self.player.Jump()

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
