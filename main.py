import pygame
from constants import *

BLACK = (0,0,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
