import os
from config.config_utils import resource_path

SOUNDS_PATH =  resource_path("assets/sounds/")
BACKGROUND_SOUND = os.path.join(SOUNDS_PATH, '723909_background.wav')
# SHOOTING_SOUND = os.path.join(SOUNDS_PATH, '154867__johnny-leung__laser-shot.wav')
# HIT_SOUND = os.path.join(SOUNDS_PATH, '209379__cabbit__hit-sound.wav')
# EXPLOSION_SOUND = os.path.join(SOUNDS_PATH, '154867__johnny-leung__laser-shot.wav')