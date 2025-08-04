import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroids import *
from asteroidfield import *
from shot import *

pygame.init()
clock = pygame.time.Clock()

dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    asteroidfield = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots)

    game = 1
    while game == 1:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in list(asteroids):
            for shot in list(shots):
                if shot.collision(asteroid):
                    print("Collision detected")
                    shot.kill()
                    asteroid.kill()
                    print(f"Shots reminaing: {len(shots)}")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
