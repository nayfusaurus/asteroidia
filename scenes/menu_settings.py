# import pygame
# import sys
# import os
# from scenes.menu_utils import draw_text

# # --- Initialze fonts ---
# pygame.font.init()


# # --- Settings Menu Function ---
# def settings_menu():
#     """
#     This function runs the settings menu loop.
#     It allows changing resolution and volume.
#     """
#     global game_state, screen, SCREEN_WIDTH, SCREEN_HEIGHT, current_volume

#     resolutions = [(800, 600), (1024, 768), (1280, 720)]
#     res_buttons = []
#     button_y = 200
#     for res in resolutions:
#         res_buttons.append(pygame.Rect(screen.get_width() / 2 - 150, button_y, 300, 50))
#         button_y += 70

#     while game_state == 'settings':
#         mx, my = pygame.mouse.get_pos()
#         screen.fill(BLACK)

#         draw_text('Settings', title_font, WHITE, screen, screen.get_width() / 2, 80, center=True)

#         # Draw Resolution Options
#         draw_text('Resolution', button_font, WHITE, screen, screen.get_width() / 2, 150, center=True)
#         for i, rect in enumerate(res_buttons):
#             res_text = f"{resolutions[i][0]} x {resolutions[i][1]}"
#             color = LIGHT_GRAY if rect.collidepoint((mx, my)) else GRAY
#             pygame.draw.rect(screen, color, rect, border_radius=10)
#             draw_text(res_text, button_font, WHITE, screen, rect.centerx, rect.centery, center=True)

#         # Draw Volume Control
#         draw_text('Volume', button_font, WHITE, screen, screen.get_width() / 2, 420, center=True)
#         volume_down_rect = pygame.Rect(screen.get_width() / 2 - 100, 470, 50, 50)
#         volume_up_rect = pygame.Rect(screen.get_width() / 2 + 50, 470, 50, 50)
        
#         pygame.draw.rect(screen, GRAY, volume_down_rect, border_radius=10)
#         pygame.draw.rect(screen, GRAY, volume_up_rect, border_radius=10)
#         draw_text('-', title_font, WHITE, screen, volume_down_rect.centerx, volume_down_rect.centery, center=True)
#         draw_text('+', title_font, WHITE, screen, volume_up_rect.centerx, volume_up_rect.centery, center=True)
        
#         # Display current volume
#         volume_display_rect = pygame.Rect(screen.get_width() / 2 - 40, 470, 80, 50)
#         pygame.draw.rect(screen, BLACK, volume_display_rect)
#         draw_text(f"{int(current_volume * 100)}%", button_font, WHITE, screen, volume_display_rect.centerx, volume_display_rect.centery, center=True)


#         # Back Button
#         back_button_rect = pygame.Rect(screen.get_width() / 2 - 100, 550, 200, 50)
#         back_color = LIGHT_GRAY if back_button_rect.collidepoint((mx, my)) else GRAY
#         pygame.draw.rect(screen, back_color, back_button_rect, border_radius=10)
#         draw_text('Back', button_font, WHITE, screen, back_button_rect.centerx, back_button_rect.centery, center=True)

#         # Event Handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     if back_button_rect.collidepoint((mx, my)):
#                         game_state = 'main_menu' # Go back to main menu
                    
#                     # Handle resolution change
#                     for i, rect in enumerate(res_buttons):
#                         if rect.collidepoint((mx, my)):
#                             SCREEN_WIDTH, SCREEN_HEIGHT = resolutions[i]
#                             screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
#                             # We must return to the main menu to redraw buttons correctly
#                             game_state = 'main_menu'

#                     # Handle volume change
#                     if volume_down_rect.collidepoint((mx, my)):
#                         current_volume = max(0.0, current_volume - 0.1)
#                         pygame.mixer.music.set_volume(current_volume)
#                     if volume_up_rect.collidepoint((mx, my)):
#                         current_volume = min(1.0, current_volume + 0.1)
#                         pygame.mixer.music.set_volume(current_volume)

#         pygame.display.update()

import pygame
import sys
from scenes.menu_utils import draw_text
from config.fonts import MENU_FONT
from config.colors import BLACK, WHITE, GRAY, LIGHT_GRAY, GREEN, BLUE
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT

title_font = pygame.font.Font(MENU_FONT, 74)
button_font = pygame.font.Font(MENU_FONT, 50)

def settings_menu(screen ): #,current_settings):
    """
    This function runs the settings menu loop.
    It allows changing resolution and volume.
    Returns the new settings and the next game state.
    """
    # Unpack current settings
    temp_width, temp_height = SCREEN_WIDTH, SCREEN_HEIGHT #current_settings['resolution']
    temp_volume = 0.4 #current_settings['volume']
    
    # Make local copies for temporary changes
    selected_resolution = (temp_width, temp_height)

    resolutions = [(800, 600), (1024, 768), (1280, 720)]
    
    # --- UI Element Positions ---
    # Volume slider
    slider_width = 300
    slider_height = 20
    slider_x = (screen.get_width() - slider_width) / 2
    slider_y = 500
    slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)
    
    knob_radius = 15
    knob_x = slider_x + int(temp_volume * slider_width)
    knob_rect = pygame.Rect(knob_x - knob_radius, slider_y - (knob_radius - slider_height/2), knob_radius * 2, knob_radius * 2)

    dragging_volume = False
    
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill(BLACK)

        # --- Draw Title and Controls ---
        draw_text('Settings', title_font, WHITE, screen, screen.get_width() / 2, 50, center=True)
        draw_text('Controls', button_font, WHITE, screen, screen.get_width() / 2, 100, center=True)
        draw_text('W, A, S, D - Movement', button_font, WHITE, screen, screen.get_width() / 2, 150, center=True)
        draw_text('SPACE - Shoot', button_font, WHITE, screen, screen.get_width() / 2, 190, center=True)

        # --- Draw Resolution Options ---
        draw_text('Resolution', button_font, WHITE, screen, screen.get_width() / 2, 250, center=True)
        res_button_y = 290
        res_buttons = []
        for res in resolutions:
            res_rect = pygame.Rect(screen.get_width() / 2 - 150, res_button_y, 300, 50)
            res_buttons.append((res, res_rect))
            
            # Highlight currently selected resolution
            if selected_resolution == res:
                pygame.draw.rect(screen, GREEN, res_rect, border_radius=10)
            else:
                pygame.draw.rect(screen, GRAY, res_rect, border_radius=10)
            
            res_text = f"{res[0]} x {res[1]}"
            draw_text(res_text, button_font, WHITE, screen, res_rect.centerx, res_rect.centery, center=True)
            res_button_y += 60

        # --- Draw Volume Control ---
        draw_text('Volume', button_font, WHITE, screen, screen.get_width() / 2, 490, center=True)
        # Slider bar
        pygame.draw.rect(screen, GRAY, slider_rect, border_radius=10)
        # Knob
        knob_x = slider_x + int(temp_volume * slider_width)
        knob_rect.centerx = knob_x
        pygame.draw.rect(screen, BLUE, knob_rect, border_radius=10)
        # Volume percentage
        draw_text(f"{int(temp_volume * 100)}%", button_font, WHITE, screen, slider_x + slider_width + 70, slider_y + 10, center=True)


        # --- Draw Back and Save Buttons ---
        back_button_rect = pygame.Rect(screen.get_width() / 2 - 220, 600, 200, 50)
        save_button_rect = pygame.Rect(screen.get_width() / 2 + 20, 600, 200, 50)
        
        # Highlight on hover
        back_color = LIGHT_GRAY if back_button_rect.collidepoint((mx, my)) else GRAY
        save_color = LIGHT_GRAY if save_button_rect.collidepoint((mx, my)) else GRAY
        
        pygame.draw.rect(screen, back_color, back_button_rect, border_radius=10)
        pygame.draw.rect(screen, save_color, save_button_rect, border_radius=10)
        
        draw_text('Back', button_font, WHITE, screen, back_button_rect.centerx, back_button_rect.centery, center=True)
        draw_text('Save', button_font, WHITE, screen, save_button_rect.centerx, save_button_rect.centery, center=True)

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Button Clicks
                    if back_button_rect.collidepoint((mx, my)):
                        # return current_settings, 'main_menu'   Return original settings
                        return 'main_menu'

                    if save_button_rect.collidepoint((mx, my)):
                        new_settings = {'resolution': selected_resolution, 'volume': temp_volume}
                        # return new_settings, 'main_menu'  Return new settings
                        return 'main_menu'

                    # Resolution selection
                    for res, rect in res_buttons:
                        if rect.collidepoint((mx, my)):
                            selected_resolution = res
                            
                    # Volume slider drag start
                    if knob_rect.collidepoint((mx, my)) or slider_rect.collidepoint((mx,my)):
                        dragging_volume = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging_volume = False
            
            if event.type == pygame.MOUSEMOTION:
                if dragging_volume:
                    # Update volume based on mouse position
                    knob_x = mx
                    # Clamp the position to the slider bounds
                    knob_x = max(slider_x, min(knob_x, slider_x + slider_width))
                    temp_volume = (knob_x - slider_x) / slider_width
                    temp_volume = round(temp_volume, 2)


        pygame.display.update()
