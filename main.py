import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot

x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT/2

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        for asteroid in asteroids:
            if player.colliding(asteroid):
                print("Game Over!")
                pygame.quit()
                return

        screen.fill(BLACK)
        for item in drawables:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
