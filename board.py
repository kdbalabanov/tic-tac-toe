from tile import Tile
from settings import *


class Board:
    height = HEIGHT
    width = WIDTH
    rows = ROWS
    columns = COLUMNS
    tiles = []

    def __init__(self, screen):
        self.screen = screen

    def init_tiles(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.tiles.append(Tile(row, column))

    def draw_grid(self):
        for tile in self.tiles:
            tile.draw(self.screen)

    def handle_click(self, mouse_pos):
        for tile in self.tiles:
            if tile.x + tile.size > mouse_pos[0] > tile.x and tile.y + tile.size > mouse_pos[1] > tile.y:
                tile.marking = "X"
