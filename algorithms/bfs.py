"""
Breadth-First Search (BFS) pathfinding algorithm implementation.
"""
import pygame
from collections import deque
import sys
from .utils import reconstruct_path

def bfs_algorithm(draw, grid, start, end):
    """
    Breadth-First Search algorithm implementation.
    Guarantees the shortest path in an unweighted grid.
    """
    open_set = deque([start])
    came_from = {}
    visited = {start}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = open_set.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            if neighbour not in visited:
                came_from[neighbour] = current
                visited.add(neighbour)
                open_set.append(neighbour)
                neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False