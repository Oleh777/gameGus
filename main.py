import random

import pygame

from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

from pygame.constants import QUIT

import sys


pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 600
WIDTH = 1000
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0, 0, 0)
COLOR_ENEMY = (10, 100, 200)
COLOR_BONUS = (100, 200, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill((COLOR_WHITE))
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_move_rihgt = [1, 0]
player_move_top = [0, -1]
player_move_left = [-1, 0]

def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_ENEMY)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-5, -1), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (25, 25)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_BONUS)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 3)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_BONUS, 1000)

enemies = []
bonuses = []

while True: 

    FPS.tick(920)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
           

    FPS.tick(620)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        
    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()


    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_rihgt)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_top)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)


    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
    # enemy_rect = enemy_rect.move(enemy_move)
        
    

    main_display.blit(player, player_rect)

    # main_display.blit(enemy, enemy_rect)
    print(len(enemies))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom < 0:
            bonuses.pop(bonuses.index(bonus))
