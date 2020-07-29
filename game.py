import settings
import pygame as pg
import os
from tkinter import Tk
from tkinter import messagebox
import sys
from board import Board


class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pg.init()
        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.board = Board(self.screen)
        self.board.init_tiles()
        self.current_player = settings.PLAYER_X

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.board.draw_grid()
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.board.is_tile_updated(pg.mouse.get_pos(), self.current_player):
                        self.update_player_turn()
            if event.type == pg.QUIT:
                self.quit()

    def update_player_turn(self):
        if self.current_player == settings.PLAYER_X:
            self.current_player = settings.PLAYER_O
        elif self.current_player == settings.PLAYER_O:
            self.current_player = settings.PLAYER_X

    def show_message(self):
        Tk().wm_withdraw()
        messagebox.showinfo(settings.TITLE, self.current_player + ' has won!')
