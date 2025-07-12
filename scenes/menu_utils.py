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