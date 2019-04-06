from tile import *

class Board():
    def __init__(self, height, width, screen):
        self._height = height
        self._width = width
        self._screen = screen
        self._tiles = []

    def init_tiles(self, num, size, color):
        for i in range(num):
            self._tiles.append(Tile(size, 0, 0, color))

    def draw_tiles(self):
        for tile in self._tiles:
            tile.draw(self._screen)

    @property
    def tiles(self):
        return self._tiles