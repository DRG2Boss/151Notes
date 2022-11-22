import arcade
import random


class ShipGoldWindow (arcade.Window):
    #  __init__ is used to declare variables we want to use throughout the ENTIRE class.
    def __init__(self, width=1200, height=1000):
        super().__init__(width, height, "Get the Gold")
        self.ship = None
        self.score = 0
        self.goals = arcade.SpriteList()
        self.sound = None
        self.throw_sound = None

    def setup(self):
        self.ship = arcade.Sprite("W9-pirate-galleon.png")
        self.ship.center_y = 200
        self.ship.center_x = 50
        self.sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.throw_sound = arcade.load_sound(":resources:sounds/lose1.wav")
        for time in range(7):
            pile = arcade.Sprite("W9-gold-coins-large.png")
            pile.center_x = random.randint(50, 1150)
            pile.center_y = random.randint(50, 950)
            self.goals.append(pile)

    def on_update(self, delta_time: float):
        collected_gold = arcade.check_for_collision_with_list(self.ship, self.goals)
        if collected_gold:
            arcade.play_sound(self.sound)
            self.score += len(collected_gold)
            for coin_pile in collected_gold:
                self.goals.remove(coin_pile)

    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        self.goals.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        pile = arcade.Sprite("W9-gold-coins-large.png")
        pile.center_x = self.ship.center_x
        pile.center_y = self.ship.center_y - 74
        self.goals.append(pile)
        arcade.play_sound(self.throw_sound)
