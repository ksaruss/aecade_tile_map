import generation_map
import statistics
import arcade
import math
import random

from opensimplex import OpenSimplex

g = OpenSimplex(2333)



v = []

# for i in range(100):
#     v.append([0] * 100)
#     for j in range(100):
#         v[i][j] = generation_map.elevation(i*-1, j*7, g)

ROW_COUNT = 500
COLUMN_COUNT = 500

WIDTH = 2
HEIGHT = 2
MARGIN = 0

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.list_tile = arcade.SpriteList()
        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        v = []
        for row in range(ROW_COUNT):
            v.append([0] * COLUMN_COUNT)
            for column in range(COLUMN_COUNT):
                v[row][column] = generation_map.elevation(row / ROW_COUNT - 0.5, column / COLUMN_COUNT - 0.5, g)
                if v[row][column][0] < 0.35:
                    color = (0, 255, 255)
                elif 0.35 <= v[row][column][0] < 0.7:
                    if v[row][column][1] < 0.4 and v[row][column][0] > 0.4:
                        color = (189, 183, 107)
                    elif 0.4 <= v[row][column][1] < 0.6 and v[row][column][0] > 0.5:
                        color = (173, 255, 47)
                    else:
                        color = (0, 100, 0)
                else:
                    color = (0, 0, 0)

                tile = arcade.SpriteSolidColor(WIDTH, HEIGHT, color)
                tile.center_x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                tile.center_y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                self.list_tile.append(tile)

    def on_draw(self):
        self.clear()
        self.list_tile.draw()


game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
