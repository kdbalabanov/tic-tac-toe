import pygame as pg
from settings import *


class Tile:
    size = TILESIZE
    color = WHITE
    marking = ' '
    marking_color = BLACK

    def __init__(self, row, column):
        self.x = row * self.size
        self.y = column * self.size
        self.rect = pg.Rect(self.x + 1, self.y + 1, self.size - 1, self.size - 1)
        self.font = pg.font.Font(pg.font.get_default_font(), self.size)

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        self.draw_mark(screen)

    def draw_mark(self, screen):
        text = self.font.render(self.marking, True, self.marking_color)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text, text_rect)
