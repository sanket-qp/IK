"""
Consider a row of n coins of values v , . . ., v .
We play a game against an opponent by alternating turns.
In each turn, a player selects either the first or last coin from the row,
    removes it from the row permanently, and receives the value of the coin.

Determine the maximum possible amount of money we can definitely win if we move first.

Example: coins given are [8, 15, 3, 7]
Answer: 23

Player 1 picks 7
Player 2 picks 8
Player 1 picks 15
Player 2 picks 3
Player 1 wins with score of 22

Greedy approach wont work:
Player 1 picks 8
Player 2 picks 15
Player 1 picks 7
Player 2 picks 3
max sum is 18 which is less than maximum possible score 22

In this case, it's easy to create DP solution from recursion approach.
Definition: DP(i, j) returns the maximum score from coins i to j

Direction: Lower i depends on Higher i
           and Higher j depends on Lower j

           so for i we'll go from end to start
           for j we'll go from start to end

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


def coin_play_recursive(coins):
    def __coin_play(coins, start, end):
        if start == end:
            return coins[start]

        # if we just have two coins, then pick the max
        if abs(end - start) == 1:
            return max(coins[start], coins[end])

        # choice1, userA picks the coin from start
        # in this case, userB will try to maximize from (start + 1, end)
        # userB can either pick (start+1) or (end)
        # if userB picks start+1 then userA will have minimum from (start+2, end)
        # if userB picks end then userA will have minimum from (start+1, end-1)
        choice1 = coins[start] + min(__coin_play(coins, start + 2, end), __coin_play(coins, start + 1, end - 1))

        # choice2, userA picks the coin from end
        # in this case userB will try to maximize from (start, end-1)
        # if userB picks start then userA will have minimum from (start+1, end-1)
        # if userB picks end-1 then userA will have minimum from (start, end-2)
        choice2 = coins[end] + min(__coin_play(coins, start + 1, end - 1), __coin_play(coins, start, end - 2))
        return max(choice1, choice2)

    score = __coin_play(coins, 0, len(coins) - 1)
    return score


def coin_play_DP(coins):
    dp_table = [[0] * len(coins) for _ in range(len(coins))]
    n = len(coins)
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp_table[i][j] = coins[i]
            else:
                # minimum in (start+2, end)
                option1 = dp_table[i + 2][j] if i < n - 2 else sys.maxint
                # minimum from (start+1, end-1)
                option2 = dp_table[i + 1][j - 1] if i < n - 1 and j > 0 else sys.maxint
                # minimum from (start, end-2)
                option3 = dp_table[i][j - 2] if j > 1 else sys.maxint
                dp_table[i][j] = max(coins[i] + min(option1, option2), coins[j] + min(option2, option3))
    return dp_table[0][n - 1]


def main():
    coins = [8, 15, 3, 7]
    # coins = [8, 15, 3, 7, 1, 10, 44, 12, 22]
    ans_recursive = coin_play_recursive(coins)
    ans_dp = coin_play_DP(coins)
    print ans_recursive
    print ans_dp
    assert 22 == ans_recursive
    assert ans_dp == ans_recursive


if __name__ == '__main__':
    main()
