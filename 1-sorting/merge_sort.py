"""
Implementation of merge sort
"""
import math
import random

def _merge(arrA, startIdxA, endIdxA, arrB, startIdxB, endIdxB):
    mergedArr = []
    idxA = startIdxA
    idxB = startIdxB
    while idxA <= endIdxA and idxB <= endIdxB:
        if arrA[idxA] <= arrB[idxB]:
            mergedArr.append(arrA[idxA])
            idxA += 1
        else:
            mergedArr.append(arrB[idxB])
            idxB += 1

    while idxA <= endIdxA:
        mergedArr.append(arrA[idxA])
        idxA += 1

    while idxB <= endIdxB:
        mergedArr.append(arrB[idxB])
        idxB += 1

    return mergedArr

def merge(arrA, arrB):
    #print arrA
    #print arrB
    return _merge(arrA, 0, len(arrA)-1, arrB, 0, len(arrB)-1)


def _mergesort(arr, startIdx, endIdx):

    if startIdx >= endIdx:
        return [arr[startIdx]]

    # potential integer overflow by following formula as startIdx and endIdx could be large numbers
    # mid = int(math.floor((startIdx + endIdx)/2))

    # alternate formula
    mid = int(math.floor(startIdx + ((endIdx - startIdx)/2)))

    arrA = _mergesort(arr, startIdx, mid)
    arrB = _mergesort(arr, mid+1, endIdx)
    return merge(arrA, arrB)

def mergesort(arr):
    return _mergesort(arr, 0, len(arr)-1)

def main():
    arrA = [1,3,5,7]
    arrB = [2,4,6,8]
    assert merge(arrA, arrB) == [1,2,3,4,5,6,7,8]

    arrA = [44]
    arrB = [4]
    assert merge(arrA, arrB) == [4, 44]

    arrA = [92, 99, 100]
    arrB = [37]
    assert merge(arrA, arrB) == [37, 92, 99, 100]

    arrA = sorted([random.randint(50, 100) for _ in range(random.randint(0, 10))])
    arrB = sorted([random.randint(25, 150) for _ in range(random.randint(0, 20))])
    assert merge(arrA, arrB) == sorted(arrA + arrB)

    arr = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
    assert mergesort(arr) == sorted(arr)

if __name__ == "__main__":
    main()