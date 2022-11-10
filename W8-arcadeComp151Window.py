import arcade


class Comp151Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.target = None

    def setup(self):
        self.player = arcade.Sprite("f1-ship1-6.png")
        self.target = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
        self.player.center_x = 500
        self.player.center_y = 500
        self.target.center_x = 600
        self.target.center_y = 500

    def on_update(self, time_since_update):
        pass

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.target.draw()
        arcade.finish_render()
