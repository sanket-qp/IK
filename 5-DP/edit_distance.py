"""
Definition:
DP(i, j) Minimum distance to convert word1[i:] to word2[j:], we are dealing with suffixes here
so to find complete distance between two strings we need DP(0, 0)


Direction:
DP(0, 0) depends on DP(1:, 0) OR DP(0, 1:) or DP(1: 1:)
so lower i depends on higher i and lower j depends on higher j
We need to fill the dp_table from higher i to loewr i and higher j to lower j
"""

import sys


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


def edit_distance_recursive(word1, word2, memo):
    if (word1, word2) in memo:
        return memo[(word1, word2)]

    if not word1 or not word2:
        return abs(len(word2) - len(word1))

    if word1 == word2:
        return 0

    # add a char in word1
    choice1 = edit_distance_recursive(word1, word2[1:], memo) + 1
    # delete a char in word1
    choice2 = edit_distance_recursive(word1[1:], word2, memo) + 1
    # replace a char in word1
    choice3 = edit_distance_recursive(word1[1:], word2[1:], memo) + (1 if word1[0] != word2[0] else 0)
    ans = min(choice1, choice2, choice3)
    memo[(word1, word2)] = ans
    return ans


def edit_distance_DP(word1, word2):
    dp_table = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    for i in range(len(word1), -1, -1):
        for j in range(len(word2), -1, -1):
            if i == len(word1):
                # last row
                dp_table[i][j] = len(word2[j:])
            elif j == len(word2):
                # last column
                dp_table[i][j] = len(word1[i:])
            else:
                choice1 = dp_table[i][j + 1] + 1
                choice2 = dp_table[i + 1][j] + 1
                choice3 = dp_table[i + 1][j + 1] + (0 if word1[i] == word2[j] else 1)
                dp_table[i][j] = min(choice1, choice2, choice3)

    print_grid(dp_table)

    # let's also find the path we've taken
    i = j = 0
    transition = 'final'
    path = [(i, j, transition)]
    while i < len(word1) - 1 or j < len(word2) - 1:
        val = dp_table[i][j]

        # if word1[i] != word2[j] that means we have performed some operation
        if word1[i] != word2[j]:
            # find out which one of the adjacent cells have value = va-1
            if (dp_table[i + 1][j]) == val - 1:
                transition = 'deleted:%s' % (word1[i])
                i = i + 1
            elif (dp_table[i][j + 1]) == val - 1:
                transition = 'added:%s' % (word2[j])
                j = j + 1
            else:
                transition = 'replaced: (%s-%s)' % (word1[i], word2[j])
                i = i + 1
                j = j + 1
        else:
            transition = 'skipped:%s' % word2[j]
            i = i + 1
            j = j + 1

        path.append((i, j, transition))

    print path
    return dp_table[0][0]


def main():
    memo = {}
    w1 = "kitten"
    w2 = "sitting"
    w1 = "hello"
    w2 = "yellow"
    ans_recursive = edit_distance_recursive(w1, w2, memo)
    print "ans_recursive", ans_recursive
    ans_dp = edit_distance_DP(w1, w2)
    print "ans_dp", ans_dp
    # assert 3 == ans_recursive
    # assert ans_recursive == ans_dp


if __name__ == '__main__':
    main()
