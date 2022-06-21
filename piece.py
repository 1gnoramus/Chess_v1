import pygame
import math
from utils import scale_image
from constants import WIDTH, HEIGHT, BLACK, ROWS, RED, CELL_SIZE, COLS, WHITE


class ChessPiece:
    PADDING = 15
    OUTLINE = 2


    def __init__(self, row, col, image):
        self.row = row
        self.col = col
        self.image = image
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = CELL_SIZE * self.col + CELL_SIZE // 2
        self.y = CELL_SIZE * self.row + CELL_SIZE // 2

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.image)

# class PAWN(ChessPiece):
#
#     def __init__(self, row, col):
#         self.row = row
#         self.col = col
#         self.x = 0
#         self.y = 0
#         self.calc_pos()
#
#     def calc_pos(self):
#         self.x = CELL_SIZE * self.col + CELL_SIZE // 2
#         self.y = CELL_SIZE * self.row + CELL_SIZE // 2
#
#     def draw(self, win):
#         win.blit(self.image, (self.x, self.y))

