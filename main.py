import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__":
    main()