import pygame
from utils import scale_image

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
CELL_SIZE = 100

WHITE, BLACK, RED, GREEN = (255,255,255), (0,0,0),(255,0,0),(0,255,0)

W_PAWN = scale_image(pygame.image.load('imgs/pawn.png'),0.2)
W_ROOK = scale_image(pygame.image.load('imgs/rook.png'),0.2)
W_KNIGHT = scale_image(pygame.image.load('imgs/chess-piece.png'),0.2)
W_BISHOP = scale_image(pygame.image.load('imgs/bishop.png'),0.2)
W_QUEEN = scale_image(pygame.image.load('imgs/queen.png'),0.2)
W_KING = scale_image(pygame.image.load('imgs/king.png'),0.2)
