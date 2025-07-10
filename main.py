import sys
import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player
from entities.asteroid import Asteroid
from scenes.asteroidfield import AsteroidField
from entities.shot import Shot
from scenes.menu import main_menu


# # --- Main Game Loop Function ---
# def game_loop():
#     """
#     This is the main game loop.
#     Replace the contents with your actual game logic.
#     """

def main():
    print("Starting Asteroids!")

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    game_state = 'main_menu'
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
        
        if game_state == 'main_menu':
        # Call the main_menu function. It will run its own loop until a
        # button is clicked, at which point it returns the next state.
            game_state = main_menu(screen)
    
        elif game_state == 'settings':
            # Here you would call your settings function
            # For example: game_state = settings_menu()
            # settings_menu() 
            print("Settings menu")
        
        elif game_state == 'game':
            # Here you would call your main game function
            # For example: game_state = game_loop()
            # game_loop()
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
        else:
            print("Invalid game state!")
            return pygame.QUIT


if __name__ == "__main__":
    main()