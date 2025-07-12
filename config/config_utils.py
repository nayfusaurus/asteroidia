import os
import sys

# --- Define paths ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and when bundled """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)