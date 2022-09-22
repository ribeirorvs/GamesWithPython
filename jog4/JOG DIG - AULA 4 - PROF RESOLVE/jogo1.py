import random
import pygame
from pygame.locals import *
from sys import exit
from vector2 import Vector2

background_image_filename = 'sushiplate.jpg' 
sprite_image_filename = 'fugu.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
pexe2 = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
position2 = Vector2(0.0, 200.0)
speed = 250
heading = Vector2()


def RandomMove(max):
    return random.randrange(0,max)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            destination_x = event.pos[0] - sprite.get_width()/2.0 
            destination_y = event.pos[1] - sprite.get_height()/2.0 
            destination = (destination_x, destination_y)

            
            heading = Vector2.from_points(position, destination) 
            heading.normalize()

    screen.blit(background, (0,0))
    screen.blit(sprite, (position.x, position.y))
    screen.blit(pexe2, (position2.x, position2.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed 
    position += heading * distance_moved 
    position2 += heading * distance_moved
    pygame.display.update()
