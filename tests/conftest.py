import sys
import os
from unittest.mock import MagicMock

# Set dummy SDL drivers so pygame.init() doesn't error on headless/audio-less systems
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
pygame.init()

# Patch mixer before game is imported so Game.__init__ doesn't need real audio hardware
pygame.mixer.Sound = MagicMock(return_value=MagicMock())
pygame.mixer.music = MagicMock()

# Add repo root to sys.path so all source modules are importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
