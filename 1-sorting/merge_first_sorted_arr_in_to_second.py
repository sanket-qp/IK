"""
Given two arrays:
1) arr1 of size n, which contains n positive integers sorted in increasing order.
2) arr2 of size (2*n) (twice the size of first), which contains n positive integers sorted in increasing order in its first half.
Second half of this array arr2 is empty. (Empty elements are marked by 0).
Write a function that takes these two arrays, and merges the first one into second one, resulting in an increasingly sorted array of (2*n) positive integers.

Approach:
         Move the 0s in the 2nd array to the beginning of the array
         Then start merging from start of the first array with 2nd half of 2nd array
         and keep adding results to the beginning of the 2nd array

         Time Complexity: O(n)
         Space Complexity: no additional space is used
"""

import random

def merge(arr1, arr2):

    # move all the elements of arr2 to the back half of the array
    j = len(arr1)
    # all 0s start from j to len(arr2)
    for i in range(len(arr1)):
        arr2[j] = arr2[i]
        j += 1

    # now start merging begining for arr1 with 2nd half of arr2
    # keep adding sorted elements to the begining of arr2
    i = 0
    j = len(arr1) #2nd pointer starts from n
    result_idx = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr2[result_idx] = arr1[i]
            result_idx += 1
            i += 1
        else:
            arr2[result_idx] = arr2[j]
            result_idx += 1
            j += 1

    while i < len(arr1):
        arr2[result_idx] = arr1[i]
        result_idx += 1
        i += 1

    while j < len(arr2):
        arr2[result_idx] = arr2[j]
        result_idx += 1
        j += 1


def main():
    N = 10
    arr1 = sorted([random.randint(1, 20) for _ in range(N)])
    arr2 = [0] * N
    arr3 = sorted([random.randint(1, 20) for _ in range(N)])
    arr4 = arr3 + arr2
    temp = sorted(arr1 + arr3)
    merge(arr1, arr4)
    assert temp == arr4


if __name__ == '__main__':
    main()