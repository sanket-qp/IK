"""
https://leetcode.com/problems/range-sum-query-2d-immutable/

Approach: Keep a sum table for every row
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sum_table = self.populateSumTable(matrix)
        print self.sum_table

    def populateSumTable(self, matrix):
        sum_table = [[0] * len(matrix[row]) for row in range(len(matrix))]
        for row in range(len(matrix)):
            _sum = 0
            for col in range(len(matrix[row])):
                _sum += matrix[row][col]
                sum_table[row][col] = _sum
        return sum_table

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        _sum = 0
        for row in range(row1, row2 + 1):
            _sum += self.sum_table[row][col2]
            if col1 > 0:
                _sum -= self.sum_table[row][col1 - 1]
        return _sum


def main():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    soln = NumMatrix(matrix)
    print soln.sumRegion(2, 1, 4, 3)

    matrix = [[-4, -5]]
    soln = NumMatrix(matrix)
    print soln.sumRegion(0, 0, 0, 0)
    print soln.sumRegion(0, 0, 0, 1)
    print soln.sumRegion(0, 1, 0, 1)


if __name__ == '__main__':
    main()
