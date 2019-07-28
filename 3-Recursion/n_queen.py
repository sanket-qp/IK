"""
The n-queen problem is the problem of placing n chess queens on an n * n chessboard, so that no two queens attack each other.

Your task is to find ALL possible arrangements for the n-queen problem.

You have to solve this problem using recursion.
(There may be other ways of solving this problem, but for the purpose of this exercise, please use recursion only).

A queen can move horizontally, vertically, or diagonally.

Approach: We'll try to place a Queen on each cell of the grid and recurse with rest of the board
          If we find a combination where there are N queens on the board, we add it to the results
          We backtrack, mark the cell empty and export other combinations
"""

import sys

EMPTY = 'E'
QUEEN = 'Q'


def print_board(board):
    """
    prints the given board on the screen
    """
    for r in range(len(board)):
        for c in range(len(board[r])):
            # sys.stdout.write("| %c (%d, %d) " % (board[r][c], r, c))
            sys.stdout.write("| %c  " % (board[r][c]))
            if c == len(board[r]) - 1:
                sys.stdout.write("|")

        print ""


def get_diagonal_cells(board, R, C):
    """
    returns a list of diagonal cells of given row and column
    """
    cells = []
    # go up, left
    row, col = R, C
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        cells.append((row, col))

    # go down, right
    row, col = R, C
    while row < len(board) - 1 and col < len(board) - 1:
        row += 1
        col += 1
        cells.append((row, col))

    # go up, right
    row, col = R, C
    while row > 0 and col < len(board) - 1:
        row -= 1
        col += 1
        cells.append((row, col))

    # go down, left
    row, col = R, C
    while row < len(board) - 1 and col > 0:
        row += 1
        col -= 1
        cells.append((row, col))

    return cells


def can_be_placed(board, R, C):
    """
    decides if a Queeen can be placed at given row and column
    """

    # check for row and col
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == R and board[row][col] == QUEEN:
                return False
            if col == C and board[row][col] == QUEEN:
                return False

    # check for diagonals
    for row, col in get_diagonal_cells(board, R, C):
        if board[row][col] == QUEEN:
            return False

    return True


def all_queens(board):
    total_queens = 0
    cells = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == QUEEN:
                cells.append((row, col))
                total_queens += 1
    return (True, cells) if total_queens == len(board) else (False, cells)


def __n_queens(board, row, col, result):
    done, cells = all_queens(board)
    if done:
        result.append(cells)
        print_board(board)
        print "---------------------------------"
        return

    if row >= len(board):
        return

    for col in range(len(board)):
        if can_be_placed(board, row, col):
            board[row][col] = QUEEN
            __n_queens(board, row + 1, col, result)
            board[row][col] = EMPTY


def n_queens(board):
    result = []
    __n_queens(board, 0, 0, result)
    return result


def get_board(N):
    return [[EMPTY] * N for _ in range(N)]


def main():
    N = 4
    board = get_board(N)

    R, C = 2, 2
    board[R][C] = QUEEN
    assert False is can_be_placed(board, 2, 2)
    assert False is can_be_placed(board, 1, 1)
    assert True is can_be_placed(board, 3, 0)
    assert True is can_be_placed(board, 0, 1)
    assert True is can_be_placed(board, 1, 0)
    assert False is can_be_placed(board, 1, 1)

    board = get_board(N)
    result = n_queens(board)
    expected = [[(0, 1), (1, 3), (2, 0), (3, 2)], [(0, 2), (1, 0), (2, 3), (3, 1)]]
    assert expected == result


if __name__ == '__main__':
    main()
