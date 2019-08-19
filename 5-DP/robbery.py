"""
There are n houses built in a line, each of which contains some value in it.
A thief is going to steal the maximal value in these houses,
but he cannot steal in two adjacent houses because the owner of a stolen house
will tell his two neighbors on the left and right side.

What is the maximal stolen value?

For example, if there are four houses with values [6, 1, 2, 7], the maximal stolen value
is 13, when the first and fourth houses are stolen.

DP Approach:
    Let's define: DP(i) = maximum value at given house_i
    So we need to find DP(N) where N is the number of total houses

    Recurrence Relationship:
        DP(i) = Max(DP(j) for j < i and j is not adjacent to i) + value(i) # choice1
                    OR
                    value(i) # choice2, where we skip the previous houses)


"""

import random


def rob_maximum_recursive(values):
    def __rob_maximum(values, i, taken, result):
        if i >= len(values):
            houses = []
            total_value = 0
            for house, value in taken:
                houses.append(house)
                total_value += value
            result.append((total_value, houses))
            return

        # choice1, steal from the current house
        # and choose the next possible house
        taken.append((i, values[i]))
        # we can't pick the next house, so skip by 2
        __rob_maximum(values, i + 2, taken, result)
        taken.pop()

        # choice2, skip the current house
        __rob_maximum(values, i + 1, taken, result)

    result = []
    taken = []
    __rob_maximum(values, 0, taken, result)
    ## print result
    return max(result)


def rob_maximum_DP(values):
    dp_table = [-1] * len(values)
    for i in range(len(values)):
        if i == 0:
            dp_table[i] = values[i]
        else:
            # find the maximum from previous valid houses
            max_from_previous = -1
            for j in range(0, i - 1):
                if dp_table[j] > max_from_previous:
                    max_from_previous = dp_table[j]

            choice1 = max_from_previous + values[i]
            choice2 = values[i]
            dp_table[i] = max(choice1, choice2)

    ## print "dp_table", dp_table
    return max(dp_table)


def main():
    values = [6, 1, 2, 7]
    total_value_recursive, houses_recursive = rob_maximum_recursive(values)
    total_value_dp = rob_maximum_DP(values)
    assert 13 == total_value_recursive
    assert [0, 3] == houses_recursive
    assert total_value_recursive == total_value_dp

    values = [10, 20, 30, 40, 50, 60]
    total_value_recursive, houses_recursive = rob_maximum_recursive(values)
    total_value_dp = rob_maximum_DP(values)
    assert 120 == total_value_recursive
    assert [1, 3, 5] == houses_recursive
    assert total_value_recursive == total_value_dp

    values = [12, 10, 1, 2, 999, 1000]
    total_value_recursive, houses_recursive = rob_maximum_recursive(values)
    total_value_dp = rob_maximum_DP(values)
    assert 1014 == total_value_recursive
    assert [0, 3, 5] == houses_recursive
    assert total_value_recursive == total_value_dp

    N = 6
    values = [random.randint(1, 20) for _ in range(N)]
    print values
    # values = [17, 8, 8, 3, 10, 13]
    total_value_recursive, houses_recursive = rob_maximum_recursive(values)
    total_value_dp = rob_maximum_DP(values)
    print total_value_recursive, houses_recursive
    assert total_value_recursive == total_value_dp


if __name__ == '__main__':
    main()
