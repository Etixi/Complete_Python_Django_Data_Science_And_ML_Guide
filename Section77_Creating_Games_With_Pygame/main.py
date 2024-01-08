import sys
import pygame

print()
print("Introduction to Pygame and Creating the Game Window " + "\n" +
      "===================================================")
print()


pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first Pygame")

while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()