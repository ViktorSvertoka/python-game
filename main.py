import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
import random


pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

font = pygame.font.SysFont("Verdana", 20)

main_surface = pygame.display.set_mode(screen)

player = pygame.Surface((20, 20))
player.fill(WHITE)
player_rect = player.get_rect()
player_speed = 5


def create_enemy():
    enemy = pygame.Surface((20, 20))
    enemy.fill(RED)
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []


def create_bonus():
    bonus = pygame.Surface((20, 20))
    bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(0, width), -height, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]


CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

scores = 0

bonuses = []

is_working = True

while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    pressed_keys = pygame.key.get_pressed()

    main_surface.fill(BLACK)

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True, WHITE), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if ball_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].top > height:
            bonuses.pop(bonuses.index(bonus))

        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

        if pressed_keys[K_DOWN] and player_rect.bottom < height:
            player_rect = player_rect.move(0, player_speed)

        if pressed_keys[K_UP] and player_rect.top > 0:
            player_rect = player_rect.move(0, -player_speed)

        if pressed_keys[K_RIGHT] and player_rect.right < width:
            player_rect = player_rect.move(player_speed, 0)

        if pressed_keys[K_LEFT] and player_rect.left > 0:
            player_rect = player_rect.move(-player_speed, 0)

    pygame.display.flip()
