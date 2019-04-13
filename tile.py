import pygame as pg


class Tile:
    def __init__(self, size, x, y, color, marking_color):
        self._size = size
        self._x = x
        self._y = y
        self._color = color
        self._marking = " "
        self._marking_color = marking_color
        self._rect = pg.Rect(self._x + 1, self._y + 1, self._size - 1, self._size - 1)
        self._font = pg.font.Font(pg.font.get_default_font(), self._size)

    def draw(self, screen):
        pg.draw.rect(screen, self._color, self._rect)
        self.draw_mark(screen)

    def draw_mark(self, screen):
        text = self._font.render(self._marking, True, self._marking_color)
        text_rect = text.get_rect()
        text_rect.center = self._rect.center
        screen.blit(text, text_rect)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, xval):
        self._x = xval

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, yval):
        self._y = yval

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, sizeval):
        self._size = sizeval

    @property
    def marking(self):
        return self._marking

    @marking.setter
    def marking(self, markingval):
        self._marking = markingval
