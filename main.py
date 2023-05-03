import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 650
WIDTH = 1100

FONT = pygame.font.SysFont('Arial', 35, True)

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0, 0, 0)
COLOR_ENEMY = (10, 100, 200)
COLOR_BONUS = (100, 200, 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

player = pygame.image.load('player.png', "gus") #pygame.Surface(player_size)
player_size = player.get_size()
player_rect = pygame.Rect(100, 150, *player_size) #player.get_rect()
player_move_down = [0, 9]
player_move_rihgt = [9, 0]
player_move_top = [0, -9]
player_move_left = [-9, 0]

def create_enemy():
    enemy = pygame.image.load('enemy.png') #pygame.Surface(enemy_size)
    enemy_size = enemy.get_size()
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT-100), *enemy_size)
    enemy_move = [random.randint(-4, -1), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus = pygame.image.load('bonus.png') #pygame.Surface(bonus_size)
    bonus_size = bonus.get_size()
    bonus_rect = pygame.Rect(random.randint(0, WIDTH-150), -200, *bonus_size)
    bonus_move = [0, random.randint(2, 4)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 4000)

CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_BONUS, 2000)

enemies = []
bonuses = []
score = 0

playing = True
while playing: 

    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
              
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()  

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

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

        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player, player_rect)

    # print(len(enemies))
    # print(len(bonuses))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < -180:
            enemies.pop(enemies.index(enemy))

    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT + 240:
            bonuses.pop(bonuses.index(bonus))