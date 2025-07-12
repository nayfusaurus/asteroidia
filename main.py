import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from scenes.menu_main import main_menu
from scenes.menu_settings import settings_menu
from scenes.game_play import game_loop

def main():
    print("Starting Asteroids!")

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = 'main_menu'

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
            game_state = settings_menu(screen) 
            
        elif game_state == 'game':
            # Here you would call your main game function
            # For example: game_state = game_loop()
            # game_loop()
            game_state = game_loop(screen)
        else:
            print("Invalid game state!")
            return pygame.QUIT


if __name__ == "__main__":
    main()