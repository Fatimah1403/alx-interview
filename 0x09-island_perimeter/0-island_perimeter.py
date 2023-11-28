#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
        The grid is completely surrounded by water
        There is only one island (or nothing).
        The island doesn’t have “lakes” (water inside
        that isn’t connected to the water surrounding the island).
    """
    total_perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0  # Check if grid is not empty

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # increment its four sides (top, bottom, left, and right)
                total_perimeter += 4

                # check for the top neighbor if is land
                if row > 0 and grid[row - 1][col] == 1:
                    total_perimeter -= 2

                # check for bottom
                if row < rows - 1 and grid[row + 1][col] == 1:
                    total_perimeter -= 2

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    total_perimeter -= 2

                # Check right neighbor
                if col < cols - 1 and grid[row][col + 1] == 1:
                    total_perimeter -= 2

    return total_perimeter
