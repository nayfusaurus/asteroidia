import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # updatable.add(player,asteroid)
    # drawable.add(player,asteroid)
    # asteroids.add(asteroid)

    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    Shot.containers = (shots, updatable, drawable) # type: ignore
    AsteroidField.containers = updatable # type: ignore
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable) # type: ignore

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)


    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for thing in asteroids:
            if thing.collision_check(player):
                print("Game over!")
                return pygame.QUIT
            for shot in shots:
                if thing.collision_check(shot):
                    print("Asteroid destroyed!")
                    thing.split()
                    shot.kill()
                
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__":
    main()