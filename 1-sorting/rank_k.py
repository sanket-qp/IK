"""
Given an array of integers, find an element of rank K

Questions to ask:
no duplicates
rank(1) in [3, 0, 1, 6] => 0
rank(2) in [3, 0, 1, 6] => 1
rank(3) in [3, 0, 1, 6] => 3
rank(4) in [3, 0, 1, 6] => 6
"""
import random

def partition(arr, left, right):
    pivot_idx = left
    pivot = arr[pivot_idx]
    while left < right:
        while left <= right and arr[left] <= pivot:
            left += 1

        while right >=  left and arr[right] > pivot:
            right -= 1

        if right > left:
            arr[left], arr[right] = arr[right], arr[left]

    partition_idx = right
    arr[pivot_idx], arr[partition_idx] = arr[partition_idx], arr[pivot_idx]
    return partition_idx


def rank(arr, k):
    if k < 1 or k > len(arr):
        raise Exception("invalid k, k must be <= %s" % len(arr))

    # one quicksort partition call puts the pivot element at the right index
    # so we can binary search the rank based on this fact
    found = False
    start = 0
    end = len(arr) - 1
    while not found:
        partition_idx = partition(arr, start, end)
        if partition_idx == k-1:
            return arr[partition_idx]
        elif k > partition_idx:
            start = partition_idx + 1
        else:
            end = partition_idx - 1

def main():
    arr = [3, 0, 1, 6]
    assert rank(arr, 1) == 0
    assert rank(arr, 4) == 6

    arr = [random.randint(0, 100) for _ in range(10)]
    temp = sorted(arr[:])
    for idx, element in enumerate(temp):
        assert rank(arr, idx+1) == element

if __name__ == "__main__":
    main()