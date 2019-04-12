from tile import *

class Board():
    def __init__(self, height, width, screen, rows, columns):
        self._height = height
        self._width = width
        self._screen = screen
        self._rows = rows
        self._columns = columns
        self._tiles = []

    def init_tiles(self, size, color):
        for row in range(self._rows):
            for column in range(self._columns):
                self._tiles.append(Tile(size, row * size, column * size, color))

    def draw_grid(self):
        for tile in self._tiles:
            tile.draw(self._screen)
