
import sys
import pygame

print()
print("Placing Rectangle In the Middle of Game Window " + "\n" +
      "===================================================")
print()



pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first Pygame")
rect_width, rect_height = 100, 200
rect_x = screen_width / 2 - rect_width / 2
rect_y = screen_height / 2 - rect_height / 2
rect_color = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((32, 52, 71))
    pygame.draw.rect(screen, (0, 255, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()