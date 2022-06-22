import time

import pygame
import math
from sup import scale_image

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 60
ROWS = 8
COLS = 8

win = pygame.display.set_mode((WIDTH,HEIGHT))
white, black, red, green, blue = (255,255,255), (0,0,0),(255,0,0),(0,255,0), (0,0,255)
win.fill(white)

W_PAWN = scale_image(pygame.image.load('imgs/pawn.png'),0.115)
W_ROOK = scale_image(pygame.image.load('imgs/rook.png'),0.115)
W_KNIGHT = scale_image(pygame.image.load('imgs/chess-piece.png'),0.115)
W_BISHOP = scale_image(pygame.image.load('imgs/bishop.png'),0.115)
W_QUEEN = scale_image(pygame.image.load('imgs/queen.png'),0.115)
W_KING = scale_image(pygame.image.load('imgs/king.png'),0.115)

class ChessBoard:

    def __init__(self):
        self.board_length = 8
        CELL_SIZE = 60

    def draw_chess_board(self, win):

        count = 0
        for i in range (1, self.board_length+1):
            for j in range (1, self.board_length+1):
                if count % 2 ==0:
                    pygame.draw.rect(win, white, [CELL_SIZE * j, CELL_SIZE* i, CELL_SIZE, CELL_SIZE])
                else:
                    pygame.draw.rect(win, black, [CELL_SIZE * j, CELL_SIZE * i, CELL_SIZE, CELL_SIZE])
                count+=1
            count -=1
        pygame.draw.rect(win, (black), [CELL_SIZE, CELL_SIZE, self.board_length * CELL_SIZE, self.board_length * CELL_SIZE], 1)

class ChessPiece:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        pass

    def move(self, row, col ):
        self.col = col
        self.row = row


    def eat(self):
        pass

class Pawn (ChessPiece):

    def __init__(self,x,y, image):
        self.x = x
        self.y = y
        self.cell_size = CELL_SIZE
        self.start_pos = [60,420]
        self.image = image
        self.pawns = [1]

    def draw_pawn(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                win.blit(self.image, (self.x, self.y))
        # i = 0
        # while self.start_pos[0] < 540:
        #     win.blit(self.image, (self.x, self.y))
        #     self.start_pos[0] += 60
        #     self.x+=self.cell_size
        #     i +=1
        #     self.pawns.append(i)

    def move_pawn(self):
        pos = pygame.mouse.get_pos()
        row = pos[0]//60
        col = pos[1]//60
        self.x = self.pawns[row] * CELL_SIZE + CELL_SIZE // 2
        self.y = self.pawns[col] * CELL_SIZE + CELL_SIZE // 2
        if self.y == 420:
            pygame.draw.rect(win, red, [self.x, self.y,
                                            self.cell_size, self.cell_size])
            pygame.draw.rect(win, green, [self.x, self.y-60,
                                            self.cell_size, self.cell_size],6)
            pygame.draw.rect(win, green, [self.x, self.y - 120,
                                              self.cell_size, self.cell_size],6)
            win.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(win, green, [self.x, self.y - 60,
                                              self.cell_size, self.cell_size], 6)
        print(row)
        pygame.draw.circle(win, (255, 0, 0), pos, 5)


def redrawGameWindow():
    # win.blit(win,(0,0))
    white_pawn.draw_pawn(win)

    pygame.display.update()

board = ChessBoard()
white_pawn = Pawn(60, 420, W_PAWN)
board.draw_chess_board(win)


run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            white_pawn.move_pawn()
        redrawGameWindow()
pygame.quit()
