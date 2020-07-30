import tictactoe.settings as settings
import pytest
from tictactoe.tile import Tile
import pygame as pg


pg.init()


@pytest.fixture
def my_tile():
    return Tile(1, 2)


def test_tile_x(my_tile):
    x = 1 * settings.TILE_SIZE
    assert my_tile.x == x


def test_tile_y(my_tile):
    y = 2 * settings.TILE_SIZE
    assert my_tile.y == y


def test_tile_row(my_tile):
    assert my_tile.row == 1


def test_tile_column(my_tile):
    assert my_tile.column == 2


def test_tile_marking(my_tile):
    assert my_tile.marking == settings.EMPTY


def test_tile_update_marking(my_tile):
    assert my_tile.is_marking_updated(settings.PLAYER_O)
    assert my_tile.marking == settings.PLAYER_O


def test_tile_overwrite_marking(my_tile):
    assert my_tile.is_marking_updated(settings.PLAYER_X)
    assert not my_tile.is_marking_updated(settings.PLAYER_O)
