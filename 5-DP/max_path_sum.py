"""
Given a grid, find the maximum sum of a path from (0, 0) to (M, N) which has the maximum sum
You can only go DOWN or RIGHT from the current cell in the grid
(Grid only has positive numbers)


Step 1: Identify the dimension of the DP table
        DP table here will be 2 Dimension as the value at each cell (i.e. max sum) represents the State, which needs 2 indices

Step 2: Pre populate the table for the independent/minimum/base cases

Step 3: Figure out the direction (low to high / high to low)

Step 4: Define recurrence relationship
        F(i, j) returns the maximum sum by following a path which ends at (i, j)
        e.g F(N-1, M-1) = max sum at the end of the grid

Step 5: return the result from the cell of a DP table
"""

import random
import sys

EMPTY = None


def get_empty_grid(NUM_ROWS, NUM_COLS):
    return [[EMPTY] * NUM_COLS for _ in range(NUM_ROWS)]


def get_grid_with_random_numbers(NUM_ROWS, NUM_COLS):
    return [[random.randint(0, 100) for c in range(NUM_COLS)] for _ in range(NUM_ROWS)]


def get_grid(NUM_ROWS, NUM_COLS, fill=False):
    if not fill:
        return get_empty_grid(NUM_ROWS, NUM_COLS)
    else:
        return get_grid_with_random_numbers(NUM_ROWS, NUM_COLS)


def print_grid(grid):
    """
    prints the given board on the screen
    """
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            # sys.stdout.write("| %c (%d, %d) " % (board[r][c], r, c))
            sys.stdout.write("| %3s  " % (grid[r][c]))
            if c == len(grid[r]) - 1:
                sys.stdout.write("|")

        print ""


def max_sum_recursive(grid, NUM_ROWS, NUM_COLS, i, j):
    # out of the grid
    if i == NUM_ROWS or j == NUM_COLS:
        return 0

    # choice1: go DOWN
    max_sum_down = max_sum_recursive(grid, NUM_ROWS, NUM_COLS, i + 1, j)
    # choice2: go RIGHT
    max_sum_right = max_sum_recursive(grid, NUM_ROWS, NUM_COLS, i, j + 1)

    # return max of two choices
    return max(max_sum_down, max_sum_right) + grid[i][j]


def max_sum_DP(grid, NUM_ROWS, NUM_COLS):
    dp_table = get_grid(NUM_ROWS + 1, NUM_COLS + 1)

    # Step 3: Direction from low to high
    # fill the table up based on the dependencies of the cells
    # cell (i, j) depends on the cell on top and cell on left
    # cell(i, j) can be calculated from cell(i-1, j) and cell(i, j-1)
    # so for loop starts from i -> NUM_ROWS and j -> NUM_COLS
    for row in range(0, NUM_ROWS + 1):
        for col in range(0, NUM_COLS + 1):
            if row == 0 or col == 0:
                dp_table[row][col] = 0
            else:
                max_sum_top = dp_table[row - 1][col]
                max_sum_left = dp_table[row][col - 1]
                dp_table[row][col] = max(max_sum_left, max_sum_top) + grid[row - 1][col - 1]

    print_grid(dp_table)
    # Also find such path using dp_table
    # to find out the path, we need to analyze how do we fill the dp_table
    # each cell, we pick the maximum from the cell on top or cell on left
    # we should be able to traverse the dp_table and figure out which cell we have picked

    # basically we reverse the actions we did during building dp_table
    # by deducting value of grid cell from max_sum we know by adding this value of the grid cell
    # we could have reached the current cell in the dp_table

    # start from the last cell and trace the path back by picking up the cells we chose
    row = NUM_ROWS
    col = NUM_COLS
    path = []
    path.append((row - 1, col - 1))
    while row != 1 or col != 1:
        grid_value = grid[row - 1][col - 1]
        max_sum_top = dp_table[row - 1][col] - grid_value
        max_sum_left = dp_table[row][col - 1] - grid_value
        if max_sum_top > max_sum_left:
            row -= 1
            path.insert(0, (row - 1, col - 1))
        else:
            col -= 1
            path.insert(0, (row - 1, col - 1))

    # first cell should also be in the path
    return dp_table[NUM_ROWS][NUM_COLS], path


def main():
    N = 5
    M = 4
    grid = get_grid(N, M, True)
    print_grid(grid)
    print ""
    max_sum_1 = max_sum_recursive(grid, N, M, 0, 0)
    max_sum_2, path = max_sum_DP(grid, N, M)
    path_str = " -> ".join("%s" % grid[x][y] for x, y in path)
    print ""
    print path_str
    assert max_sum_1 == max_sum_2


if __name__ == '__main__':
    main()
