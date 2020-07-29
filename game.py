import pygame as pg
import sys
from settings import *
from board import Board


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.board = Board(self.screen)
        self.board.init_tiles()
        self.current_player = PLAYER_X

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.board.draw_grid()
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.board.handle_click(pg.mouse.get_pos(), self.current_player)
                    self.update_player_turn()
            if event.type == pg.QUIT:
                self.quit()

    def update_player_turn(self):
        if self.current_player == PLAYER_X:
            self.current_player = PLAYER_O
        elif self.current_player == PLAYER_O:
            self.current_player = PLAYER_X
