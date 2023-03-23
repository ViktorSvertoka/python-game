import pygame
from pygame. constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

print(screen)

main_surface = pygame.display.set_mode(screen)

is_working = True

ball = pygame.Surface((20, 20))
ball.fill((255, 255, 255))

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False


    main_surface.blit(ball, (100, 100))

    # main_surface.fill((255, 155, 200))

    pygame.display.flip()