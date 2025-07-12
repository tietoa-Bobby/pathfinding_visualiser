"""
Utility functions shared across different pathfinding algorithms,
such as the heuristic for A* and the path reconstruction function.
"""

def h(p1, p2):
    """
    Heuristic function (Manhattan distance) for A*.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    """
    Draws the final path from end to start by backtracking.
    """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()