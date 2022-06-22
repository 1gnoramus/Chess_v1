import pygame

def scale_image(img, factor):
    size = round(img.get_width()*factor), round(img.get_height()*factor)
    return pygame.transform.scale(img, size)

def position_image(img):
    position = img.get_p