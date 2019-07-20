"""
Given an integer array arr of size N, find all magical triplets in it.
Magical triplet is the group of 3 integers, whose sum is zero.
Note that magical triplets may or may not be made of consecutive numbers in arr.


Approach:
    We'll use a lookup table where key is the number in an array and value is the frequency of that number
    now we'll iterate through each number using two loops, sum them up and try to find -sum in the look up table.
    if we have -sum in the table then we found 3 numbers whose sum is 0

    to avoid duplicates, we'll store sorted tuples in a set
"""

import random
from collections import defaultdict

lookup_table = defaultdict(int)

def reset_lookup_table(arr):
    global lookup_table
    lookup_table = defaultdict(int)
    for n in arr:
        lookup_table[n] += 1

def magical_triplets(arr):
    global  lookup_table
    triplets = set()
    for i in range(len(arr)):
        reset_lookup_table(arr)
        current_n = arr[i]
        for j in range(0, len(arr)):
            if j == i:
                continue
            current_j = arr[j]
            _sum = current_n + current_j
            # if sum equals to current_n or current_j then we must have more than 1 occurrence of -sum in look up table
            # so that we don't match same number in the triplet
            expected_count = 2 if (-_sum == current_n or -_sum == current_j) else 1
            if lookup_table.get(-_sum, 0) == expected_count:
                lookup_table[_sum] -= 1
                triplets.add(tuple(sorted((current_n, current_j, -_sum, ))))
                break

    return triplets

def main():
    N = 10
    arr = [random.randint(-100, 100) for _ in range(3, N)]
    # arr = [-6, 10, 3, -4, 1, 9]
    arr = [10, 20, -6, -4, -30]
    arr = [-100, 20, -6, -4, 100, 0, 6, -14]
    print arr
    print magical_triplets(arr)

if __name__ == '__main__':
    main()