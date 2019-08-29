"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:

Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]
]
Output: 3

Hint: The number of elements in the given matrix will not exceed 10,000.
"""


class Solution(object):

    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # we'll keep dp_table per direction
        directions = ('diagonal', 'horizontal', 'vertical', 'antidiagonal')
        dp_table = {}
        for d in directions:
            dp_table[d] = [[0] * len(M[row]) for row in range(len(M))]

        functions = {
            'horizontal': lambda row, col: (row, col - 1),
            'vertical': lambda row, col: (row - 1, col),
            'diagonal': lambda row, col: (row - 1, col - 1),
            'antidiagonal': lambda row, col: (row - 1, col + 1)
        }

        max_lines = 0
        result_row = result_col = -1
        result_direction = None

        for row in range(len(M)):
            for col in range(len(M[row])):
                if M[row][col] == 0:
                    continue

                for d in directions:
                    dp_row, dp_col = functions[d](row, col)
                    if dp_row < 0 or dp_row >= len(M):
                        dp_table[d][row][col] = M[row][col]
                    elif dp_col < 0 or dp_col >= len(M[row]):
                        dp_table[d][row][col] = M[row][col]
                    else:
                        dp_table[d][row][col] = dp_table[d][dp_row][dp_col] + 1

                    if dp_table[d][row][col] > max_lines:
                        max_lines = dp_table[d][row][col]
                        result_row, result_col = row, col
                        result_direction = d

        # print result_direction
        # print result_row, result_col
        # print max_lines
        #
        # for d in directions:
        #     print d, dp_table[d]

        return max_lines


def main():
    soln = Solution()
    matrix = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
    assert 3 == soln.longestLine(matrix)

    matrix = [
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    assert 4 == soln.longestLine(matrix)

    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert 0 == soln.longestLine(matrix)


if __name__ == '__main__':
    main()
