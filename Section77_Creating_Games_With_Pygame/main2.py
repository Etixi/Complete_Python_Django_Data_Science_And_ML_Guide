import sys
from random import randint

import pygame

print()
print("Modifying Background Color of the Game Surface " + "\n" +
      "===================================================")
print()


clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first Pygame")


while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((randint(0, 255),randint(0, 255), randint(0, 255)))
    # screen.fill(pygame.Color("green"))
    # screen.fill((250, 0, 0))
    pygame.display.update()
    clock.tick(1)