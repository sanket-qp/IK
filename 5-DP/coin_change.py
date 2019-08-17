"""
Given a total amount T and array of denominations (changes). Find out minimum number of coins are required to generate T
    F(18, [1, 9, 13]) = 2 (2 coins of 9)

Step 1: Identify the dimensions of the DP table
        1 dimension, an array of amounts from 0 to T

Step 2: Pre populate the table with base cases
        dp_table[0] = 0 (0 coins needed to get change of 0)

Step 3: Figure out the direction (from low to high i.e. 0 to T)

Step 4: Define recurrence relationship

        F(T) = Min(F(T-D_i for each denomination in D iff T > D_i)) + 1
             = 0 if T = 0


Step 5: Return the result from the cell of a DP table


Approach 1: From the recurrence relationship
            F(T) = Min(F(T-D_i for each denomination in D iff T > D_i)) + 1

            For T = 18 and D = [1, 9, 13]
            We know that T(18) depends on T(18-1), T(18-9) and T (18-13)

            So Higher T depends on lower Ts.
            so we can simple start from 0 and go up to T to populate the dp_table


Approach 2: at any given D_i,
            we can either choose it to find F(T-D_i), We want to keep the i same as (T-Di) might use the same denomination
            OR
            we can skip that denomination and find F(T) with remaining denominations

            so the recurrence relationship will look as follows
            F(T, i) = minimum coins required for generating T with all denominations starting at i
            F(6, 0) = minimum coins required to generate 6 with all denominations
            F(T, i) = min (F(T-Di, i)+1, F(T, i+1))

            For DP, We can take a small example
            T = 6, D = {2, 3}
            F(6, 0) depends on F(4, 0) i.e (T-Di, i) and F(6, 1) i.e (T, i+1)
            F(4, 0) depends on F(2, 0) and F(4, 1)
            F(2, 0) depends on F(0, 0) and F(2, 1)

            F(T, 0) depends on lower Ts (T-Di, i) and higher i (T, i+1)

            Direction:
            so we can start building the table from t = 0 -> T and i = len(D) -> 0
"""

import random
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


def coin_change_recursive(T, D):
    if T == 0:
        return 0

    _min = sys.maxint
    for d in D:
        if d <= T:
            _min = min(_min, (coin_change_recursive(T - d, D)))

    if _min == sys.maxint:
        return _min
    else:
        return _min + 1


def xcoin_change_DP(T, D):
    dp_table = [0] * (T + 1)
    for i in range(0, T + 1):
        if i == 0:
            dp_table[i] = 0
        else:
            _min = sys.maxint
            for d in D:
                if d <= i:
                    _min = min(_min, dp_table[i - d])

            if _min == sys.maxint:
                dp_table[i] = _min
            else:
                dp_table[i] = _min + 1

    return dp_table[T]


def coin_change_DP(T, D):
    dp_table = [0] * (T + 1)
    for i in range(0, T + 1):
        if i == 0:
            dp_table[i] = 0
        else:
            _min = sys.maxint
            for d in D:
                if d <= i:
                    _min = min(_min, dp_table[i - d])

            if _min == sys.maxint:
                dp_table[i] = _min
            else:
                dp_table[i] = _min + 1

    # find picked coins
    picked_coins = []
    t = T
    while t > 0:
        temp = []
        for d in D:
            if t - d >= 0:
                # add remaining value and picked coin
                temp.append((dp_table[t - d], d))

        # find the minimum from temp that's what we chose
        _min = sys.maxint
        picked_coin = None
        for dp_value, coin in temp:
            if dp_value < _min:
                _min = dp_value
                picked_coin = coin

        picked_coins.append(picked_coin)
        t = t - picked_coin

    return dp_table[T], picked_coins


def coin_change_recursive_2(T, D, i):
    if i == len(D):
        return sys.maxint

    if T <= 0:
        return 0

    choice1 = sys.maxint
    if D[i] <= T:
        choice1 = coin_change_recursive_2(T - D[i], D, i) + 1
    choice2 = coin_change_recursive_2(T, D, i + 1)
    return min(choice1, choice2)


def xcoin_change_DP_2(T, D):
    dp_table = [[0] * (len(D) + 1) for _ in range(T + 1)]
    for t in range(T + 1):
        for i in range(len(D), -1, -1):
            if t == 0:
                dp_table[t][i] = 0
            elif i == len(D):
                dp_table[t][i] = 100
            else:
                _min = 100
                if D[i] <= t:
                    dp_table[t][i] = min(dp_table[t - D[i]][i] + 1, dp_table[t][i + 1])
                else:
                    dp_table[t][i] = _min

    print_grid(dp_table)
    return dp_table[T][0]


def coin_change_DP_2(T, D):
    dp_table = [[0] * (len(D) + 1) for _ in range(T + 1)]
    for t in range(T + 1):
        for i in range(len(D), -1, -1):
            if t == 0:
                dp_table[t][i] = 0
            elif i == len(D):
                dp_table[t][i] = 100
            else:
                _min = 100
                if D[i] <= t:
                    dp_table[t][i] = min(dp_table[t - D[i]][i] + 1, dp_table[t][i + 1])
                else:
                    dp_table[t][i] = _min

    # to find out which coins were picked, we need to back track the DP table
    # dp_table[T][0] has our answer, now we'll back track from there by
    # reversing the process

    # dp[T][0] is chosen from min (dp[T-D[0][0] + 1, dp[T][1])
    # we'll choose minimum of these two

    t = T
    i = 0
    picked_coins = []
    while t > 0 and i <= len(D):
        choice1 = dp_table[t - D[i]][i] + 1
        choice2 = dp_table[t][i + 1]

        if choice1 < choice2:
            t = t - D[i]
        else:
            i += 1

        if t != T:
            picked_coins.append(D[i])

    print_grid(dp_table)
    print picked_coins
    return dp_table[T][0], picked_coins


def main():
    NUM_OF_DENOMINATIONS = random.randint(1, 5)
    DENOMINATIONS = [random.randint(1, 100) for _ in range(NUM_OF_DENOMINATIONS)]
    TOTAL_AMOUNT = random.randint(1, 100)

    TOTAL_AMOUNT = 18
    DENOMINATIONS = [1, 9, 13]
    # DENOMINATIONS = [34, 11, 18, 99, 6]
    # TOTAL_AMOUNT = 76
    # TOTAL_AMOUNT = 6
    # DENOMINATIONS = [2, 3]

    TOTAL_AMOUNT = 91
    DENOMINATIONS = [64, 63, 29, 1]

    ans_recursive = coin_change_recursive(TOTAL_AMOUNT, DENOMINATIONS)
    ans_dp, picked_coins_dp1 = coin_change_DP(TOTAL_AMOUNT, DENOMINATIONS)

    print TOTAL_AMOUNT, DENOMINATIONS
    print ans_recursive

    assert ans_recursive == ans_dp

    ans_recursive_2 = coin_change_recursive_2(TOTAL_AMOUNT, DENOMINATIONS, 0)
    ans_dp_2, picked_coins_dp2 = coin_change_DP_2(TOTAL_AMOUNT, DENOMINATIONS)
    print ans_recursive_2

    print "dp1", ans_dp
    print "dp2", ans_dp_2

    # assert ans_recursive_2 == ans_dp_2
    # assert ans_recursive == ans_recursive_2
    # assert ans_dp == ans_dp_2

    print "picked coins dp1", picked_coins_dp1
    print "picked coins dp2", picked_coins_dp2


if __name__ == '__main__':
    main()
