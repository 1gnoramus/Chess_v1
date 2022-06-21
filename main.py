import pygame
import math
from utils import scale_image
from constants import WIDTH, HEIGHT, BLACK, ROWS, RED, CELL_SIZE, COLS, WHITE
from board import ChessBoard

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Chess Game')

board = ChessBoard()
# pawn = ChessPiece(200, 600, W_PAWN)
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    board.draw_squares(win)
    pygame.display.update()

pygame.quit()