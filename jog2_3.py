import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('img/tanque.jpg').convert()

x,y=0,0
move_x, move_y = 0,0
lastKey = 'left'

def rotate(key):
    global lastKey
    # Check if the key pressed is the same as the previous one
    if lastKey != key:
        global tank
        #Rotate to left
        if key == 'left':
            if lastKey == 'right':
                tank = pygame.transform.flip(tank, True, False)
            elif lastKey == 'up':
                tank = pygame.transform.rotate(tank, 90)
            elif lastKey == 'down':
                tank = pygame.transform.rotate(tank, 270)
        # Rotate to right
        elif key == 'right':
            if lastKey == 'left':
                tank = pygame.transform.flip(tank, True, False)
            elif lastKey == 'up':
                tank = pygame.transform.rotate(tank, 270)
            elif lastKey == 'down':
                tank = pygame.transform.rotate(tank, 90)
        # Rotate to up
        elif key == 'up':
            if lastKey == 'down':
                tank = pygame.transform.flip(tank, False, True)
            elif lastKey == 'left':
                tank = pygame.transform.rotate(tank, 270)
            elif lastKey == 'right':
                tank = pygame.transform.rotate(tank, 90)
        # Rotate to down
        elif key == 'down':
            if lastKey == 'up':
                tank = pygame.transform.flip(tank, False, True)
            elif lastKey == 'left':
                tank = pygame.transform.rotate(tank, 90)
            elif lastKey == 'right':
                tank = pygame.transform.rotate(tank, 270)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Move to Left
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                move_x=-1
                rotate('left')
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x=0
                lastKey = 'left'
        #Move to Right
        if event.type == KEYDOWN:
            if event.key==K_RIGHT:
                move_x=+1
                rotate('right')
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                move_x=0
                lastKey = 'right'
        #Move to Down
        if event.type == KEYDOWN:
            if event.key==K_DOWN:
                move_y=+1
                rotate('down')
        if event.type == KEYUP:
            if event.key == K_DOWN:
                move_y=0
                lastKey = 'down'
        #Move to Up
        if event.type == KEYDOWN:
            if event.key==K_UP:
                move_y=-1
                rotate('up')
        if event.type == KEYUP:
            if event.key == K_UP:
                move_y=0
                lastKey = 'up'

        x += move_x
        y += move_y

        screen.fill((255,255,255))
        screen.blit(tank,(x,y))

        pygame.display.update()
