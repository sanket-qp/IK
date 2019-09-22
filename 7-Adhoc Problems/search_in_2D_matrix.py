"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        def search(matrix, start_row, end_row, start_col, end_col, n):
            # print "searching: (%s, %s) to (%s, %s)" % (start_row, start_col, end_row, end_col)
            if end_row < start_row:
                return False

            if end_col < start_col:
                return False

            top_right = matrix[start_row][end_col]
            if n == top_right:
                return True
            elif n < top_right:
                end_col -= 1
            else:
                start_row += 1

            return search(matrix, start_row, end_row, start_col, end_col, n)

        return search(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, target)


def main():
    soln = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 44]
    ]

    assert True is soln.searchMatrix(matrix, 3)
    assert False is soln.searchMatrix(matrix, 33)
    assert True is soln.searchMatrix(matrix, 34)
    assert True is soln.searchMatrix(matrix, 23)
    assert True is soln.searchMatrix(matrix, 7)
    assert True is soln.searchMatrix(matrix, 44)


if __name__ == '__main__':
    main()
