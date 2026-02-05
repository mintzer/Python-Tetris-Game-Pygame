# pygame_ce compatibility shim
# pygame-ce provides the pygame module directly, not pygame_ce
# This shim allows 'import pygame_ce as pygame' to work
from pygame import *
import pygame as _pygame
# Re-export all pygame attributes
__all__ = dir(_pygame)
__version__ = _pygame.version.ver
__name__ = 'pygame_ce'
