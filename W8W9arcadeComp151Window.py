import arcade
import random


class Comp151Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.targets = arcade.SpriteList()
        self.sound = None
        self.player_dx = 0

    def setup(self):
        self.sound = arcade.load_sound("W9-elec_lightning.wav")
        self.player = arcade.Sprite("f1-ship1-6.png")
        self.player.center_x = 50
        self.player.center_y = 500
        for number in range(5):
            self.target = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
            self.target.center_x = random.randint(16, 1184)
            self.target.center_y = random.randint(16, 984)
            self.targets.append(self.target)

    def on_update(self, time_since_update):
        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 50
            arcade.play_sound(self.sound)
        for rock in self.targets:
            rock.center_y -= 2

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -3
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 3

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or arcade.key.RIGHT:
            self.player_dx = 0
