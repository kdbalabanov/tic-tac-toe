from tile import *

class Board():
    def __init__(self, height, width, screen, rows, columns):
        self._height = height
        self._width = width
        self._screen = screen
        self._rows = rows
        self._columns = columns
        self._tiles = []

    def init_tiles(self, num, size, color):
        for i in range(num):
            self._tiles.append(Tile(size, 0, 0, color))

    def draw_tiles(self):
        for tile in self._tiles:
            tile.draw(self._screen)

    def draw_grid(self):
        for i in range(self._rows):
            for j in range(self._columns):
                self._tiles[0].draw(self._screen, i, j)


    @property
    def tiles(self):
        return self._tiles