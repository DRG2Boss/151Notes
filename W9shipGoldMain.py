import arcade
# "from" calls the file name, "import" imports (duh) the class within the file.
from W9ShipGoldWindow import ShipGoldWindow


def main():
    high_seas_window = ShipGoldWindow()
    arcade.set_background_color(arcade.color.SEA_BLUE)
    high_seas_window.setup()
    arcade.run()


main()
