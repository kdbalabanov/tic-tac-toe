import settings
import pygame as pg


class Tile:
    def __init__(self, row, column):
        self.x = row * settings.TILE_SIZE
        self.y = column * settings.TILE_SIZE
        self.row = row
        self.column = column
        self.rect = pg.Rect(self.x + 1, self.y + 1, settings.TILE_SIZE - 1, settings.TILE_SIZE - 1)
        self.marking = settings.EMPTY
        self.font = pg.font.Font(pg.font.get_default_font(), settings.TILE_SIZE)

    def draw(self, screen):
        pg.draw.rect(screen, settings.WHITE, self.rect)
        self.draw_marking(screen)

    def draw_marking(self, screen):
        text = self.font.render(self.marking, True, settings.BLACK)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text, text_rect)

    def is_marking_updated(self, marking):
        if self.marking == settings.EMPTY:
            print('Updated tile at ROW: ' + str(self.row + 1) + ' and COLUMN: ' + str(self.column + 1) + ' - NEW MARKING - ' + marking)
            self.marking = marking
            return True
        return False
