"""
Maze generation algorithm using iterative Recursive Backtracking.
"""
import pygame
import random
import sys


def remove_wall(current, next_node, grid):
    """Removes the wall (node) between two other nodes."""
    c_row, c_col = current.get_pos()
    n_row, n_col = next_node.get_pos()

    # Horizontal movement
    if c_row == n_row:
        wall_col = (c_col + n_col) // 2
        grid[c_row][wall_col].reset()
    # Vertical movement
    elif c_col == n_col:
        wall_row = (c_row + n_row) // 2
        grid[wall_row][c_col].reset()


def generate_maze(draw, grid):
    """
    Generates a maze using the iterative Recursive Backtracking algorithm.
    This ensures the entire grid is traversable.
    """
    # 1. Pick a starting cell, push it to the stack
    # We must start on an odd row/col to have room for passages
    start_row = random.randrange(1, len(grid), 2)
    start_col = random.randrange(1, len(grid[0]), 2)
    start_node = grid[start_row][start_col]
    start_node.reset()

    stack = [start_node]
    visited = {start_node}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = stack[-1]

        # Find unvisited neighbours (2 cells away)
        row, col = current.get_pos()

        potential_neighbours = [
            (row - 2, col), (row + 2, col), (row, col - 2), (row, col + 2)
        ]
        random.shuffle(potential_neighbours)

        for r, c in potential_neighbours:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] not in visited:
                next_node = grid[r][c]
                remove_wall(current, next_node, grid)
                next_node.reset()
                visited.add(next_node)
                stack.append(next_node)
                break
        else:  # If no unvisited neighbour was found
            stack.pop()

        draw()