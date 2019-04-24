import pygame as pg
import sys
from settings import *
from board import Board


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.board = Board(self.screen)
        self.board.init_tiles()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        pass

    def draw_grid(self):
        self.board.draw_grid()

    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pg.mouse.get_pos()
                    self.board.handle_click(mouse_pos)
            if event.type == pg.QUIT:
                self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
