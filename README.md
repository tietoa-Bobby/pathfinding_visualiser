[![License](https://img.shields.io/github/license/tietoa-Bobby/pathfinding_visualiser?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square)](https://www.python.org/)

# Pathfinding Algorithm Visualiser

A Python application built with Pygame to visualise various pathfinding algorithms. This tool provides an interactive grid where you can set a start point, an end point, and barriers to see how different algorithms find the shortest path.

## Features
-   **Maze Generation**: Automatically generate a perfect maze using a Recursive Backtracking algorithm.
-   **Interactive Grid**: Easily draw and erase nodes (start, end, barriers) with your mouse.
-   **Multiple Algorithms**: Visualise and compare A*, Dijkstra's, Breadth-First Search (BFS), and Depth-First Search (DFS).
-   **Step-by-Step Visualisation**: Watch the algorithms work in real-time as they explore the grid.
-   **Clear UI**: On-screen instructions guide you through the controls.

## Algorithms Implemented

-   **A* Search**: An informed search algorithm that uses a heuristic to find the shortest path. It's generally the most efficient for this kind of problem.
-   **Dijkstra's Algorithm**: Finds the shortest path in a weighted graph. In this unweighted grid, it explores outwards in all directions equally based on distance from the start.
-   **Breadth-First Search (BFS)**: An uninformed search algorithm that is guaranteed to find the shortest path (by number of steps) in an unweighted grid.
-   **Depth-First Search (DFS)**: An uninformed search algorithm that explores as far as possible along each branch before backtracking. It does **not** guarantee the shortest path.

## Requirements

-   Python 3.x
-   Pygame

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/tietoa-Bobby/pathfinding_visualiser.git
    cd pathfinding_visualiser
    ```

2.  Install the required packages:
    ```bash
    pip install pygame
    ```

## How to Use

Run the main script from your terminal (ensure you are in the project directory):
```bash
python3 pathfinder.py
```

### Controls

-   **Left Mouse Click**: Place nodes. The first click is the **Start Node** (orange), the second is the **End Node** (turquoise), and subsequent clicks are **Barrier Nodes** (black).
-   **Right Mouse Click**: Erase any node.
-   **A Key**: Select **A* Search**.
-   **D Key**: Select **Dijkstra's Algorithm**.
-   **B Key**: Select **Breadth-First Search (BFS)**.
-   **S Key**: Select **Depth-First Search (DFS)**.
-   **M Key**: Generate a random maze.
-   **Spacebar**: Start the visualization for the selected algorithm.
-   **C Key**: Clear the grid and reset the board.