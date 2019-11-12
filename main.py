import pygame as game
import random
import os
from Sprite.Sprites import Player, sprite_objects
from Options.Settings import *
from Sprite.Platform import *

asset_folder = os.path.dirname(__file__)  # Cross Referenced for image from index.
image_folder = os.path.join(asset_folder, 'img')  # Cross Referenced as well from index.
dead = game.mixer.Sound('Sprite/sound/Randomize10.ogg')
hop = game.mixer.Sound('Sprite/sound/Jump.ogg')


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
        self.font = game.font.match_font(game_font)

    def begin(self):
        # Game creation function, platform creation function, added score.
        self.score_num = 0
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
                    select.kill()  # If the platforms goes below the window height, kill the object, add 5 points.
                    self.score_num += 5

        # Player Kill Function Check for rect.bottom of player
        if self.player.rect.bottom > window_height:
            self.make_ending_screen()
            self.on = False

        # Spawn brand new platforms from random number values. Keep an average number of them.
        while len(self.platforms) < 5:
            spawn = Platform(random.randrange(0, window_width - random_width),
                             random.randrange(-50, -35), random_width, 25)  # Random x and y values called
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
        self.window.fill(White)
        sprite_objects.draw(self.window)
        # Create flip display to re-draw elements, including score
        self.score_draw(str(self.score_num), 15, white_box, window_width / 2, 10)
        game.display.flip()

    def make_ending_screen(self):
        # You died screen.
        dead.play()
        self.window.fill(White)
        self.score_draw("You Died Bruh..", 50, Red, window_width / 2, window_height / 4)
        self.score_draw("Final Distance: " + str(self.score_num), 25, Orange, window_width / 2, window_height / 2)
        game.display.flip()
        self.key_STOP()

    def score_draw(self, text, size, color, x, y):
        # height score to post to screen
        font = game.font.Font(self.font, size)
        text_area = font.render(text, True, color)
        text_surface = text_area.get_rect()
        text_surface.midtop = (x, y)
        self.window.blit(text_area, text_surface)

    def startup_screen(self):
        # Screen when first turned on.
        self.window.fill(White)
        self.score_draw("Jelly-Bouncer", 50, Red, window_width * .5, window_height * .20)
        self.score_draw("Press Space-Bar for Hops, "
                        "Arrows to move, fall to...die i guess.",
                        15, Black, window_width / 1.9, window_height / 2)
        self.score_draw("Press any Key to begin Play.....", 30, Orange, window_height * .30, window_width * 1.2)
        game.display.flip()
        self.key_STOP()

    def key_STOP(self):
        paused = True
        while paused:
            self.timer.tick(game_speed)
            for routine in game.event.get():
                if routine.type == game.QUIT:
                    paused = False
                    self.on = False
                if routine.type == game.KEYUP:
                    paused = False


win = Game()
while win.alive:
    win.startup_screen()
    win.begin()

game.quit()
