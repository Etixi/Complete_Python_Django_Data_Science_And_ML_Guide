from random import randint
import sys
import pygame

print()
print("Displaying a Rectangle in The Game " + "\n" +
      "===================================================")
print()



pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first Pygame")



while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 200))
    pygame.display.update()
