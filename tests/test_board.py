import tictactoe.settings as settings
import pytest
from tictactoe.board import Board
import pygame as pg


pg.init()


@pytest.fixture
def board():
    screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    board = Board(screen)
    board.init_tiles()
    return board


def test_init_tiles(board):
    assert board.tiles
    assert len(board.tiles) == settings.GRID_SIZE * settings.GRID_SIZE


def test_is_tile_updated(board):
    assert board.is_tile_updated((10, 10), settings.PLAYER_X)
    assert board.tiles[0].marking == settings.PLAYER_X


def test_is_first_diagonal_in_winning_state(board):
    for tile in board.tiles:
        if tile.row == tile.column:
            tile.marking = settings.PLAYER_X

    assert board.is_first_diagonal_in_winning_state()
    assert board.is_in_winning_state()


def test_is_second_diagonal_in_winning_state(board):
    for i in range(0, settings.GRID_SIZE):
        for tile in board.tiles:
            if tile.row == settings.GRID_SIZE - i - 1 and tile.column == i and tile.marking == settings.EMPTY:
                tile.marking = settings.PLAYER_X

    assert board.is_second_diagonal_in_winning_state()
    assert board.is_in_winning_state()


def test_is_there_row_in_winning_state(board):
    for i in range(0, settings.GRID_SIZE):
        board.tiles[i].marking = settings.PLAYER_X

    assert board.is_there_row_in_winning_state()
    assert board.is_in_winning_state()


def test_is_there_column_in_winning_state(board):
    for i in range(0, len(board.tiles), settings.GRID_SIZE):
        board.tiles[i].marking = settings.PLAYER_O

    assert board.is_there_column_in_winning_state()
    assert board.is_in_winning_state()
