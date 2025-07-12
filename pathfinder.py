"""
Main application file for the Pathfinding Visualiser.
This script sets up the Pygame window, handles user input, and runs the selected
pathfinding algorithm on a grid.
"""

import pygame
import constants as C
from algorithms import (a_star_algorithm, dijkstra_algorithm, bfs_algorithm,
                        dfs_algorithm, generate_maze)
# --- Setup Display ---
WIN = pygame.display.set_mode((C.WIDTH, C.WIDTH + C.UI_HEIGHT))
pygame.display.set_caption("Pathfinding Algorithm Visualiser")


class Node:
    """
    Represents a single node/spot in the grid.
    """
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width  # Corrected: x corresponds to columns
        self.y = row * width  # Corrected: y corresponds to rows
        self.colour = C.WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == C.RED

    def is_open(self):
        return self.colour == C.GREEN

    def is_barrier(self):
        return self.colour == C.BLACK

    def is_start(self):
        return self.colour == C.ORANGE

    def is_end(self):
        return self.colour == C.TURQUOISE

    def reset(self):
        self.colour = C.WHITE

    def make_start(self):
        self.colour = C.ORANGE

    def make_closed(self):
        self.colour = C.RED

    def make_open(self):
        self.colour = C.GREEN

    def make_barrier(self):
        self.colour = C.BLACK

    def make_end(self):
        self.colour = C.TURQUOISE

    def make_path(self):
        self.colour = C.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])
        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        # This method is needed for the PriorityQueue to handle cases where
        # two nodes have the same f_score. Since the Node object itself is
        # not comparable, this provides a fallback comparison.
        return False


def make_grid(rows, width):
    """
    Creates the grid of Node objects.
    """
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid


def draw_grid_lines(win, rows, width):
    """
    Draws the grid lines on the window.
    """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, C.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, C.GREY, (j * gap, 0), (j * gap, width))


def draw_ui(win, selected_algo):
    """Draws the UI panel at the bottom of the screen."""
    pygame.draw.rect(win, C.WHITE, (0, C.WIDTH, C.WIDTH, C.UI_HEIGHT))
    pygame.draw.line(win, C.GREY, (0, C.WIDTH), (C.WIDTH, C.WIDTH), 2)

    algo_text = C.FONT.render(f"Algorithm: {selected_algo}", 1, C.BLACK)
    win.blit(algo_text, (10, C.WIDTH + (C.UI_HEIGHT - algo_text.get_height()) // 2))

    controls_text = C.FONT.render(
        "A/D/B/S: Select Algo | M: Maze | SPACE: Run | C: Clear", 1, C.GREY
    )
    text_rect = controls_text.get_rect(
        centery=C.WIDTH + C.UI_HEIGHT // 2, right=C.WIDTH - 10
    )
    win.blit(controls_text, text_rect)


def draw(win, grid, rows, width, selected_algo):
    """Draws everything to the window."""
    win.fill(C.WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid_lines(win, rows, width)
    draw_ui(win, selected_algo)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    """Gets the (row, col) of a mouse click from pixel coordinates."""
    gap = width // rows
    x, y = pos # Corrected: get x, y from mouse position
    row = y // gap
    col = x // gap
    return row, col


def main(win, width):
    """The main function and game loop."""

    grid = make_grid(C.ROWS, width)

    start = None
    end = None

    selected_algo_name = "A* Search"
    algorithms = {
        "A* Search": a_star_algorithm,
        "Dijkstra's": dijkstra_algorithm,
        "BFS": bfs_algorithm,
        "DFS": dfs_algorithm
    }

    run = True

    while run:
        draw(win, grid, C.ROWS, width, selected_algo_name)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # LEFT MOUSE BUTTON
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                if pos[1] < width: # Ensure click is within the grid area
                    row, col = get_clicked_pos(pos, C.ROWS, width)
                    node = grid[row][col]
                    if not start and node != end:
                        start = node
                        start.make_start()
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    elif node != end and node != start:
                        node.make_barrier()

            # RIGHT MOUSE BUTTON
            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                if pos[1] < width: # Ensure click is within the grid area
                    row, col = get_clicked_pos(pos, C.ROWS, width)
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    selected_algo_name = "A* Search"
                elif event.key == pygame.K_d:
                    selected_algo_name = "Dijkstra's"
                elif event.key == pygame.K_b:
                    selected_algo_name = "BFS"
                elif event.key == pygame.K_s:
                    selected_algo_name = "DFS"

                if event.key == pygame.K_m:
                    start = None
                    end = None
                    for row in grid:
                        for node in row:
                            node.make_barrier()

                    draw_func = lambda: draw(win, grid, C.ROWS, width, selected_algo_name)
                    generate_maze(draw_func, grid)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)

                    # Call the selected algorithm
                    selected_func = algorithms[selected_algo_name]
                    draw_func = lambda: draw(win, grid, C.ROWS, width, selected_algo_name)
                    selected_func(draw_func, grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(C.ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(WIN, C.WIDTH)