# spot.py

import pygame
from colors import (
    RED,
    GREEN,
    BLUE,
    WHITE,
    BLACK,
    GREY,
    YELLOW,
    PURPLE,
    ORANGE,
    TURQUOISE,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
)


class Spot:
    def __init__(self, row, col, width, total_rows, queen_image):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.total_rows = total_rows
        self.width = width
        self.color = WHITE
        self.neighbors = []
        self.is_queen = False
        self.queen_image = queen_image

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.is_queen

    def is_checking(self):
        return self.color == BLUE

    def is_reset(self):
        return self.color == WHITE and not self.is_queen

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.is_queen = True

    def make_checking(self):
        self.color = BLUE

    def make_reset(self):
        self.is_queen = False
        self.color = WHITE

    def draw(self, win):
        if (self.row + self.col) % 2 == 0:
            color = WHITE
        else:
            color = BLACK
        pygame.draw.rect(win, color, (self.x, self.y, self.width, self.width))
        if self.is_queen:
            win.blit(self.queen_image, (self.x, self.y))
        elif self.color != WHITE:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def __lt__(self, other):
        return False
