import sys
import os
import random
from unittest.mock import MagicMock

# Add repo root to sys.path before any game module imports are attempted
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Set dummy SDL drivers so pygame.init() doesn't error on headless/audio-less systems
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

# Seed RNG for deterministic block sequences across all tests
random.seed(42)

import pygame
pygame.init()

# Patch mixer before game is imported so Game.__init__ doesn't need real audio hardware
pygame.mixer.Sound = MagicMock(return_value=MagicMock())
pygame.mixer.music = MagicMock()
