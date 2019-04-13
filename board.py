from tile import *


class Board:
    def __init__(self, height, width, screen, rows, columns):
        self._height = height
        self._width = width
        self._screen = screen
        self._rows = rows
        self._columns = columns
        self._tiles = []

    def init_tiles(self, size, color, marking_color):
        for row in range(self._rows):
            for column in range(self._columns):
                self._tiles.append(Tile(size, row * size, column * size, color, marking_color))

    def draw_grid(self):
        for tile in self._tiles:
            tile.draw(self._screen)

    def handle_click(self, mouse_pos):
        for tile in self._tiles:
            if tile.x + tile.size > mouse_pos[0] > tile.x and tile.y + tile.size > mouse_pos[1] > tile.y:
                tile.marking = "X"
