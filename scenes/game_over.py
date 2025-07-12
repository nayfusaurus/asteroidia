import pygame
import sys
from config.fonts import MENU_FONT
from scenes.menu_utils import draw_text
from config.colors import WHITE, GRAY, LIGHT_GRAY, RED

# --- Fonts ---
title_font = pygame.font.Font(MENU_FONT, 74)
button_font = pygame.font.Font(MENU_FONT, 50)


def game_over(screen):
    """
    This function runs the game over screen loop.
    It takes the screen and fonts as arguments to draw on.
    It returns the next game state based on user actions.
    """
    # Create a semi-transparent overlay
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) # Black with 180/255 alpha transparency
    screen.blit(overlay, (0, 0))

    # Loop until the user makes a choice
    while True:
        # Get mouse position
        mx, my = pygame.mouse.get_pos()

        # Draw Title
        draw_text('Game Over', title_font, RED, screen, screen.get_width() / 2, 150, center=True)

        # Create and draw buttons
        button_width, button_height = 250, 60
        restart_button_rect = pygame.Rect((screen.get_width() / 2) - (button_width / 2), 300, button_width, button_height)
        menu_button_rect = pygame.Rect((screen.get_width() / 2) - (button_width / 2), 400, button_width, button_height)

        # Highlight button on hover
        if restart_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_GRAY, restart_button_rect, border_radius=10)
        else:
            pygame.draw.rect(screen, GRAY, restart_button_rect, border_radius=10)

        if menu_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_GRAY, menu_button_rect, border_radius=10)
        else:
            pygame.draw.rect(screen, GRAY, menu_button_rect, border_radius=10)

        # Draw button text
        draw_text('Restart', button_font, WHITE, screen, restart_button_rect.centerx, restart_button_rect.centery, center=True)
        draw_text('Main Menu', button_font, WHITE, screen, menu_button_rect.centerx, menu_button_rect.centery, center=True)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if restart_button_rect.collidepoint((mx, my)):
                        return 'game'  # Return the next state: restart the game
                    if menu_button_rect.collidepoint((mx, my)):
                        return 'main_menu'  # Return the next state: go to menu

        # Update the display
        pygame.display.update()
