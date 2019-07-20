"""
quicksort implementation
"""

import random

num_partitions = 0

def set_random_pivot(arr, left, right):
    """
    in some cases quick sort can lead to o(n^2) performance, so by experiments it's proven that
    in practice, if we choose 3 random indices and pick the element at median of those 3 random indices
    leads to O(n log n) performance in 95% of the cases

    if the array is sorted in reverse order, then it'll be partitioned n times and this will lead to O(n^2)
    """
    random_indexes = [random.randint(left, right) for _ in range(3)]
    middle_index = sorted(random_indexes)[1]
    # put element at random index as a first element, i.e. pivot
    arr[left], arr[middle_index] = arr[middle_index], arr[left]
    return left

def partition(arr, left, right, choose_random_pivot = True):
    print "partition", arr[left:right+1]
    pivot_idx = set_random_pivot(arr, left, right) if choose_random_pivot else left
    pivot = arr[pivot_idx]

    while left < right:
        # find an index on the left side which is greater than the pivot
        # so that we can move that to the right side of the array
        while (left < right and arr[left] <= pivot):
            left += 1
        # we found the left index where first element is greater than pivot


        # find an index on the right side of the array which is less than the pivot
        # so that we can move it to the left side of the array 
        while (right >= left and arr[right] > pivot):
            right -= 1
        # we found the right index where first element is less than pivot
        
        # now swap the elements so that element < pivot are on left
        # and element > pivot are on the right
        if right > left:
            arr[left], arr[right] = arr[right], arr[left]

    # now that we have scanned the whole array for elements < pivot
    # and elements > pivot and put them on the correct side of array
    # let's move the pivot to the proper index 
    partition_idx = right
    arr[pivot_idx], arr[partition_idx] = arr[partition_idx], arr[pivot_idx]
    return partition_idx

def _quicksort(arr, left, right, choose_random_pivot):
    global num_partitions
    num_partitions = 0

    if left >= right:
        return 

    # print "BEFORE PARTITION", arr[left:right+1]
    partition_idx = partition(arr, left, right, choose_random_pivot)
    # print "AFTER PARTITION", arr[left:right + 1]
    # print "===="
    _quicksort(arr, left, partition_idx - 1, choose_random_pivot)
    _quicksort(arr, partition_idx + 1, right, choose_random_pivot)

def quicksort(arr, choose_random_pivot=True):
    _quicksort(arr, 0, len(arr)-1, choose_random_pivot)

def main():
    # arr = [3, 2, 1]
    # idx = partition(arr, 0, len(arr) - 1)
    # assert idx == 2
    # assert arr == [1, 2, 3]
    #
    # arr = [4, 7, 1, 21, 6, 5, 3, 2]
    # idx = partition(arr, 0, len(arr) - 1)
    # assert idx == 3
    # assert arr == [3, 2, 1, 4, 6, 5, 21, 7]
    #
    # arr = [6, 5, 21, 7]
    # idx = partition(arr, 0, len(arr) - 1)
    # assert idx == 1
    # assert arr == [5, 6, 21, 7]

    arr = [4, 7, 1, 21, 6, 5, 3, 2]
    temp = arr[:]
    quicksort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 21]
    print "quicksort(%s) = %s" % (temp, arr)
    print "--------------------------------------"

    arr = [random.randint(0, 100) for _ in range (10)]
    temp = arr[:]
    quicksort(arr)
    assert arr == sorted (temp)
    print "quicksort(%s) = %s" % (temp, arr)
    print "--------------------------------------"

    arr = [random.randint(0, 100) for _ in range (10)]
    temp = arr[:]
    quicksort(arr)
    assert arr == sorted (temp)
    print "quicksort(%s) = %s" % (temp, arr)
    print "--------------------------------------"

    arr = [random.randint(0, 100) for _ in range(10)]
    arr = list(reversed(sorted(arr)))
    temp = arr[:]
    quicksort(arr, False)
    assert arr == sorted(temp)
    print "quicksort(%s) = %s" % (temp, arr)
    print "--------------------------------------"

    arr = [random.randint(0, 100) for _ in range(10)]
    arr = list(reversed(sorted(arr)))
    temp = arr[:]
    quicksort(arr, True)
    assert arr == sorted(temp)
    print "quicksort(%s) = %s" % (temp, arr)
    print "--------------------------------------"


if __name__ == "__main__":
    main()