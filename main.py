import pygame
from pygame. constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

print(screen)

main_surface = pygame.display.set_mode(screen)

is_working = True

ball = pygame.Surface((20, 20))
ball.fill((255, 255, 255))
bal_rect = ball.get_rect()
ball_speed = [1, 1]

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    bal_rect = bal_rect.move(ball_speed)
    main_surface.blit(ball, bal_rect)

    # main_surface.fill((255, 155, 200))
 
    pygame.display.flip()