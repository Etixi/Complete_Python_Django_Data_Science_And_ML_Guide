import sys
import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Awesome Shooter Game")

fighter_image = pygame.image.load('../images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = screen_width / 2 - fighter_width / 2
fighter_y = screen_height - fighter_height
FIGHTER_STEP = 20
fighter_is_moving_left, fighter_is_moving_right = False, False

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
                fighter_x -= FIGHTER_STEP
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
                fighter_x += FIGHTER_STEP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    pygame.display.update()