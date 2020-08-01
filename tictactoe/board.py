import tictactoe.settings as settings
from tictactoe.tile import Tile


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = []

    def init_tiles(self):
        for row in range(0, settings.GRID_SIZE):
            for column in range(0, settings.GRID_SIZE):
                self.tiles.append(Tile(row, column))

    def draw_grid(self):
        for tile in self.tiles:
            tile.draw(self.screen)

    def is_tile_updated(self, mouse_pos, marking):
        for tile in self.tiles:
            if tile.x + settings.TILE_SIZE > mouse_pos[0] > tile.x and tile.y + settings.TILE_SIZE > mouse_pos[1] > tile.y:
                return tile.is_marking_updated(marking)

    def is_in_winning_state(self):

        if self.is_first_diagonal_in_winning_state() or self.is_second_diagonal_in_winning_state():
            return True

        if self.is_there_row_in_winning_state() or self.is_there_column_in_winning_state():
            return True

        return False

    def is_first_diagonal_in_winning_state(self):
        first_diagonal = [x.marking for x in self.tiles if x.row == x.column and x.marking != settings.EMPTY]

        if len(first_diagonal) == settings.GRID_SIZE and len(set(first_diagonal)) == 1:
            return True

        return False

    def is_second_diagonal_in_winning_state(self):
        second_diagonal = []

        for i in range(0, settings.GRID_SIZE):
            for tile in self.tiles:
                if tile.row == settings.GRID_SIZE - i - 1 and tile.column == i and tile.marking != settings.EMPTY:
                    second_diagonal.append(tile.marking)

        if len(second_diagonal) == settings.GRID_SIZE and len(set(second_diagonal)) == 1:
            return True

        return False

    def is_there_row_in_winning_state(self):
        for i in range(0, settings.GRID_SIZE):
            row = [x.marking for x in self.tiles if x.row == i and x.marking != settings.EMPTY]
            if len(row) == settings.GRID_SIZE and len(set(row)) == 1:
                return True

        return False

    def is_there_column_in_winning_state(self):
        for i in range(0, settings.GRID_SIZE):
            column = [x.marking for x in self.tiles if x.column == i and x.marking != settings.EMPTY]
            if len(column) == settings.GRID_SIZE and len(set(column)) == 1:
                return True

        return False
