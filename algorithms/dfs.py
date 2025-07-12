"""
Depth-First Search (DFS) pathfinding algorithm implementation.
"""
import pygame
import sys
from .utils import reconstruct_path

def dfs_algorithm(draw, grid, start, end):
    """
    Depth-First Search algorithm implementation.
    NOTE: Does not guarantee the shortest path.
    """
    open_set = [start]  # Use a list as a stack (LIFO)
    came_from = {}
    visited = {start}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = open_set.pop()  # Get last item from the stack

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        # Reverse neighbors to make visualization more intuitive (e.g., explores down before up)
        for neighbor in reversed(current.neighbors):
            if neighbor not in visited:
                came_from[neighbor] = current
                visited.add(neighbor)
                open_set.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False