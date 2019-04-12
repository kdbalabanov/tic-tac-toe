import pygame as pg

class Tile:
    def __init__(self, size, x, y, color):
        self._size = size
        self._x = x
        self._y = y
        self._color = color
        self._rect = pg.Rect(self._x + 1, self._y + 1, self._size - 1, self._size - 1)

    def draw(self, screen):
        pg.draw.rect(screen, self._color, self._rect)

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
