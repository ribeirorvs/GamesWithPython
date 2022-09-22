import pygame
from pygame.locals import *
from pygame import Rect
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

def createRect(x, y, w, h, color):
    rect = Rect(x,y,w,h)
    surface = pygame.surface.Surface((800, 600))
    pygame.draw.rect(surface, color, rect)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        rect1 = createRect(0, 1, 10, 10, (255, 0, 0))
        screen.blit(rect1, (0, 00))


        pygame.display.update()
