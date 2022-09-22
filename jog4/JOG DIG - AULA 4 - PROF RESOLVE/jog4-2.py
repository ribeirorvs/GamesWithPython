import random
import pygame
from pygame.locals import *
from sys import exit
from vector2 import Vector2

background_image_filename = 'background.png' 
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
fish1 = pygame.image.load(sprite_image_filename).convert_alpha()
fish2 = pygame.image.load(sprite_image_filename).convert_alpha()
fish2 = pygame.transform.flip(fish1, True, False)
bubbles = []

#Create arrays to define circle objects with the following:
#index=0: initial x,y
#index=1: radius
#index=2: array usedo to move the circle [x,y]
#index=3: step count to change move direction
for i in range(8):
    bubbles.append([[random.randrange(50,590), random.randrange(540, 1000)], random.randrange(10, 50), [-1,-1], 15])

clock = pygame.time.Clock()

position1 = Vector2(300.0, 100.0)
motion1 = Vector2(1, 1)
position2 = Vector2(75.0, 23.0)
motion2 = Vector2(-1, -1)

def MoveFish(position, motion):
    if position.x + motion.x >= 490:
        motion.x = -1
        return True
    if position.y + motion.y >= 358:
        motion.y = -1
    if position.x + motion.x <= 0:
        motion.x = 1
        return True
    if position.y + motion.y <= 0:
        motion.y = 1
    
    return False

def MoveBubble(circle):
    if circle[3] > 0 :
        circle[3] -= 1
        if circle[0][0] + circle[2][0] >= 590:
            circle[2][0] = -1
        if circle[0][0] + circle[2][0] <= 50:
            circle[2][0] = 1
        circle[0][0] += circle[2][0]
        circle[0][1] += circle[2][1]
    elif circle[3] == 0:
        circle[3] = 15
        newX = random.randrange(0, 2)
        if newX == 1 :
            circle[2][0] = 1
        else :
            circle[2][0] = -1
    if circle[0][1] < -50 :
        circle[0][1] = random.randrange(540, 1000)
        circle[0][0] = random.randrange(50,590)
        circle[1] = random.randrange(10, 50)


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if MoveFish(position1, motion1) :
        fish1 = pygame.transform.flip(fish1, True, False)

    if MoveFish(position2, motion2) :
        fish2 = pygame.transform.flip(fish2, True, False)
    
    position1 += motion1
    position2 += motion2
    screen.blit(background, (0,0))
    screen.blit(fish1, (position1.x, position1.y))
    screen.blit(fish2, (position2.x, position2.y))


    for circle in bubbles:
        MoveBubble(circle)
        pygame.draw.circle(screen, (102, 238, 255), circle[0], circle[1], 3)

    time_passed = clock.tick(30)
#pygame.draw.circle(screen, 10, (random.randrange(10,630), 500), random.randrange(10, 50), 3)
    pygame.display.update()
