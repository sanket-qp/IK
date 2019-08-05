"""
Given an integer array arr of size n and a target sum k,
    you have to determine, whether there exists a non-empty group of numbers
    (numbers need not to be contiguous) in arr such that their sum equals to k.
"""


def __target_sum(arr, idx, K, taken, result):
    if K == 0:
        result.append(taken[:])
        return True

    if idx == len(arr):
        return False

    # choice1, take the current element
    # find if remaining sum present in the remaining of the array
    new_k = K - arr[idx]
    taken.append(arr[idx])
    choice1 = __target_sum(arr, idx + 1, new_k, taken, result)
    taken.pop()
    # explore if original sum is present without taking present element
    choice2 = __target_sum(arr, idx + 1, K, taken, result)
    return choice1 or choice2


def target_sum(arr, K):
    taken = []
    result = []
    possible = __target_sum(arr, 0, K, taken, result)
    return result, possible


def main():
    arr = [2, 8, -2, 1]
    K = -2
    combinations, possible = target_sum(arr, K)
    assert True is possible
    assert [[-2]] == combinations

    arr = [1, 2, -2, 6, 2]
    K = 4
    combinations, possible = target_sum(arr, K)
    assert True is possible
    assert [[2, 2], [-2, 6]] == combinations

    arr = [1, 2, -2, 6, 2]
    K = 5
    combinations, possible = target_sum(arr, K)
    assert True is possible
    assert [[1, 2, 2], [1, -2, 6]] == combinations

    arr = [1, 3, 5]
    K = 2
    combinations, possible = target_sum(arr, K)
    assert False is possible
    assert [] == combinations


if __name__ == '__main__':
    main()
