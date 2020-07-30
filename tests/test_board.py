import tictactoe.settings as settings
import pytest
from tictactoe.board import Board
import pygame as pg


pg.init()


@pytest.fixture
def my_board():
    screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    return Board(screen)


def test_board_tiles(my_board):
    assert not my_board.tiles
    assert len(my_board.tiles) == 0


def test_init_tiles(my_board):
    my_board.init_tiles()
    assert my_board.tiles
    assert len(my_board.tiles) == settings.ROWS * settings.COLUMNS


def test_is_tile_updated(my_board):
    my_board.init_tiles()
    assert my_board.is_tile_updated((10, 10), settings.PLAYER_X)
    assert my_board.tiles[0].marking == settings.PLAYER_X
