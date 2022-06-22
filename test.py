import pygame
import math



WIDTH = 600
HEIGHT = 600
win = pygame.display.set_mode((WIDTH,HEIGHT))
white = (255,255,255)

#Size of squares
size = 60

#board length, must be even
boardLength = 8
win.fill(white)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(win, (255,255,255),[size*z,size*i,size,size])
        else:
            pygame.draw.rect(win, (0,0,0), [size*z,size*i,size,size])
        cnt +=1
    #since theres an even number of squares go back one value
    cnt-=1
#Add a nice boarder
pygame.draw.rect(win,(0,0,0),[size,size,boardLength*size,boardLength*size],1)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break




# array = []
# x = pygame.image.load('imgs/pawn.png')
# y = pygame.image.load('imgs/rook.png')
# x = 0
# for i in range(1, 9):
#     for j in range(1, 9):
#         if x % 2 == 0:
#
#         else:
#
#     x+=1
#         temp.reverse()
#     array.append(temp)
#
# for i in array:
#     print(i)
    pygame.display.update()
pygame.quit()

# drawing a board
win.fill(black)
for row in range(self.board_length):
    for col in range(row % 2, self.board_length, 2):
        pygame.draw.rect(win, white, (self.cell_size * row, self.cell_size * col, self.cell_size, self.cell_size))
