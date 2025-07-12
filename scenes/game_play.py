import sys
import pygame
from entities.player import Player
from entities.asteroid import Asteroid
from scenes.asteroidfield import AsteroidField
from entities.shot import Shot
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from scenes.game_over import game_over

# --- Game Loop Function ---
def game_loop(screen):
    """
    This function runs the main game loop.
    """
    pygame.init()

    dt = 0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    Shot.containers = (shots, updatable, drawable) # type: ignore
    AsteroidField.containers = updatable # type: ignore
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable) # type: ignore

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)

    while True:
        pygame.Surface.fill(screen, (0,0,0))

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for thing in asteroids:
            if thing.collision_check(player):
                print("Game over!")
                return game_over(screen)
            for shot in shots:
                if thing.collision_check(shot):
                    print("Asteroid destroyed!")
                    thing.split()
                    shot.kill()
                
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(60)
        dt = clock.get_time() / 1000

