import pygame
from constants import *

pygame.init


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = 1

while game == 1:
    screen.fill((0,0,0))
    pygame.display.flip()

if __name__ == "__main__":
    main()
