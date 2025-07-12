"""
Centralized constants for the Pathfinding Visualizer application.
This includes colors, screen dimensions, and grid settings.
"""
import pygame

# --- Display Settings ---
WIDTH = 800
UI_HEIGHT = 50
ROWS = 50

# --- Colors ---
RED = (255, 0, 0)        # Closed Set
GREEN = (0, 255, 0)      # Open Set
WHITE = (255, 255, 255)  # Default
BLACK = (0, 0, 0)        # Barrier
PURPLE = (128, 0, 128)   # Path
ORANGE = (255, 165, 0)   # Start
GREY = (128, 128, 128)   # Grid Lines
TURQUOISE = (64, 224, 208) # End

# --- Font ---
pygame.font.init()
FONT = pygame.font.SysFont('sans-serif', 22)