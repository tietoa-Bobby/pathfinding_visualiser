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

        # Reverse neighbours to make visualization more intuitive (e.g., explores down before up)
        for neighbour in reversed(current.neighbours):
            if neighbour not in visited:
                came_from[neighbour] = current
                visited.add(neighbour)
                open_set.append(neighbour)
                neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False