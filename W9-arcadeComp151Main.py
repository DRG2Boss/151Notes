import arcade
import W8W9arcadeComp151Window


def main():
    our_window = W8W9arcadeComp151Window.Comp151Window(1200, 1000, "Arcade with a Window Class")
    our_window.setup()
    arcade.run()


main()
