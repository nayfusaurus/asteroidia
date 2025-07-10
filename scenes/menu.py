import pygame
import sys
import os

# --- Constants ---
# It's good practice to keep constants for colors, etc., in the module
# where they are most relevant, or in a dedicated config file.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (170, 170, 170)
# Define paths
ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..\\assets')
FONTS_PATH = os.path.join(ASSETS_PATH, 'fonts')
SOUNDS_PATH = os.path.join(ASSETS_PATH, 'sounds')

pygame.font.init()

#Load fonts
title_font = pygame.font.Font(os.path.join(FONTS_PATH, 'Dashhorizon.otf'), 74)
button_font = pygame.font.Font(os.path.join(FONTS_PATH, 'Dashhorizon.otf'), 50)

pygame.mixer.init()
# --- Audio ---
# Global volume setting (0.0 to 1.0)
current_volume = 0.3
pygame.mixer.music.set_volume(current_volume)

# It's good practice to handle potential errors, like a missing music file
try:
    pygame.mixer.music.load(SOUNDS_PATH+'\\723909_background.wav')
    pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely
except pygame.error:
    print("Warning: '723909_background.wav' not found. Music will not play.")

# --- Helper Function to Draw Text ---
def draw_text(text, font, color, surface, x, y, center=False):
    """
    A helper function to easily draw text on the screen.
    """
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect

# --- Main Menu Function ---
def main_menu(screen):
    """
    This function runs the main menu loop.
    It takes the screen and fonts as arguments to draw on.
    It returns the next game state based on user actions.
    """
    # Loop until the user makes a choice
    while True:
        # Get mouse position
        mx, my = pygame.mouse.get_pos()

        # Fill background
        screen.fill(BLACK)

        # Draw Title
        draw_text('Main Menu', title_font, WHITE, screen, screen.get_width() / 2, 100, center=True)

        # Create and draw buttons
        button_width, button_height = 250, 60
        start_button_rect = pygame.Rect((screen.get_width() / 2) - (button_width / 2), 250, button_width, button_height)
        settings_button_rect = pygame.Rect((screen.get_width() / 2) - (button_width / 2), 350, button_width, button_height)
        exit_button_rect = pygame.Rect((screen.get_width() / 2) - (button_width / 2), 450, button_width, button_height)

        # Highlight button on hover
        if start_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_GRAY, start_button_rect, border_radius=10)
        else:
            pygame.draw.rect(screen, GRAY, start_button_rect, border_radius=10)

        if settings_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_GRAY, settings_button_rect, border_radius=10)
        else:
            pygame.draw.rect(screen, GRAY, settings_button_rect, border_radius=10)

        if exit_button_rect.collidepoint((mx, my)):
            pygame.draw.rect(screen, LIGHT_GRAY, exit_button_rect, border_radius=10)
        else:
            pygame.draw.rect(screen, GRAY, exit_button_rect, border_radius=10)

        # Draw button text
        draw_text('Start Game', button_font, WHITE, screen, start_button_rect.centerx, start_button_rect.centery, center=True)
        draw_text('Settings', button_font, WHITE, screen, settings_button_rect.centerx, settings_button_rect.centery, center=True)
        draw_text('Exit', button_font, WHITE, screen, exit_button_rect.centerx, exit_button_rect.centery, center=True)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if start_button_rect.collidepoint((mx, my)):
                        return 'game'  # Return the next state
                    if settings_button_rect.collidepoint((mx, my)):
                        return 'settings'  # Return the next state
                    if exit_button_rect.collidepoint((mx, my)):
                        pygame.quit()
                        sys.exit()

        # Update the display
        pygame.display.update()
