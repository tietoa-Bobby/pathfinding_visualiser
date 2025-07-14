"""
Dijkstra's pathfinding algorithm implementation.
"""
import pygame
from queue import PriorityQueue
import sys
from .utils import reconstruct_path

def dijkstra_algorithm(draw, grid, start, end):
    """
    Dijkstra's pathfinding algorithm implementation.
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))  # Priority is g_score (distance from start)
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((g_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False