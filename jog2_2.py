import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('img/tanque.jpg').convert()

x,y=pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Move the tank with the mouse
        if event.type == MOUSEMOTION:
            x, y = pygame.mouse.get_pos()

        screen.fill((255,255,255))
        screen.blit(tank,(x,y))

        pygame.display.update()
