import pygame
from constants import *

BLACK = (0,0,0)

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill(BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
