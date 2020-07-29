import settings
from tile import Tile


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = []

    def init_tiles(self):
        for row in range(0, settings.ROWS):
            for column in range(0, settings.COLUMNS):
                self.tiles.append(Tile(row, column))

    def draw_grid(self):
        for tile in self.tiles:
            tile.draw(self.screen)

    def is_tile_updated(self, mouse_pos, marking):
        for tile in self.tiles:
            if tile.x + settings.TILE_SIZE > mouse_pos[0] > tile.x and tile.y + settings.TILE_SIZE > mouse_pos[1] > tile.y:
                return tile.is_marking_updated(marking)
