"""

This is a popular facebook problem.

Given K sorted arrays arr, of size N each, merge them into a new array res, such that res is a sorted array.

Assume N is very large compared to K. N may not even be known.
The arrays could be just sorted streams, for instance, timestamp streams.
All arrays might be sorted in increasing manner or decreasing manner. Sort all of them in the manner they appear in input.

Note:
Repeats are allowed.
Negative numbers and zeros are allowed.
Assume all arrays are sorted in the same order. Preserve that sort order in
output.
It is possible to find out the sort order from at least one of the arrays.

Approach 1:
    just use merge functionality of merge sort and keep sorting two lists until all of them are merged.
    Problem with this approach is, when N is very large, we are using O(N) extra space
    Time complexity is O(K*N)

Approach 2: (not implemented)
    Use heap, keep adding numbers to a heap and then retrieve them
    Problem with this approach is it also takes O(N) extra space
    Time complexity is 2 * K * O(N logN)

Approach 3:
        we keep adding numbers from each list to the heap along with the index of the source array.
        heap will help us retrieving the lowest number seen so far.
        once we retrieve the lowest number, we'll add a new number from corresponding source array to the heap.

        Example: if we remove number 2 (source_list = 1 i.e. K=1) then we'll add another number from the same
        source list to the heap

        Time Complexity: O(NK*Log(K))
        Space Complexity: O(K + NK) (K for heap, NK for result array)
"""

import sys
import heapq
import random

min_fn = lambda x, y: x <= y
max_fn = lambda x, y: x > y

def determine_sort_order(arr):
    min_index = 0
    max_index = 0
    _min = sys.maxint
    _max = -sys.maxint

    for idx, element in enumerate(arr):
        if element < _min:
            _min = element
            min_index = idx
        elif element > _max:
            _max = element
            max_index = idx
    return max_fn if min_index > max_index else min_fn

def merge_sorted_arrays(arr1, arr2, comparator):
    idx1 = 0
    idx2 = 0
    merged = []
    while (idx1 < len(arr1) and idx2 < len(arr2)):
        if comparator(arr1[idx1], arr2[idx2]):
            merged.append(arr1[idx1])
            idx1 += 1
        else:
            merged.append(arr2[idx2])
            idx2 += 1

    while idx1 <= len(arr1)-1:
        merged.append(arr1[idx1])
        idx1 += 1

    while idx2 <= len(arr2)-1:
        merged.append(arr2[idx2])
        idx2 += 1

    return merged

def merge_k_sorted_arrays(lst_of_sorted_array, K):
    if K <= 1:
        raise Exception("invalid value K, k must be >= 2")

    comparator = determine_sort_order(lst_of_sorted_array[0])

    # merge two arrays first
    merged = [] # just to save on number of objects, let's pass the result array from outside
    merged = merge_sorted_arrays(lst_of_sorted_array[0], lst_of_sorted_array[1], comparator)
    current_lst_idx = 2

    # now merged each remaining list with already sorted list
    while current_lst_idx < K:
        next_lst = lst_of_sorted_array[current_lst_idx]
        merged = merge_sorted_arrays(merged, next_lst, comparator)
        current_lst_idx += 1
    return merged

def merge_k_sorted_arrays_using_heap(lst_of_sorted_array, K):
    """
    Approach:
        we keep adding numbers from each list to the heap along with the index of the source array.
        heap will help us retrieving the lowest number seen so far.
        once we retrieve the lowest number, we'll add a new number from corresponding source array to the heap.

        Example: if we remove number 2 (source_list = 1 i.e. K=1) then we'll add another number from the same
        source list to the heap
    """
    heap = []
    if (K < 2):
        raise Exception("K should be >= 2")

    result = []
    # add first element from each list to the heap
    for lst_idx in range(K):
        if len(lst_of_sorted_array[lst_idx]) > 0:
            element_idx = 0
            element = lst_of_sorted_array[lst_idx][0]
            _tuple = (element, lst_idx, element_idx, )
            heapq.heappush(heap, _tuple)


    while len(heap) > 0:
        (element, lst_idx, element_idx) = heapq.heappop(heap)
        result.append(element)
        if element_idx < len(lst_of_sorted_array[lst_idx])-1:
            element_idx += 1
            element = lst_of_sorted_array[lst_idx][element_idx]
            _tuple = (element, lst_idx, element_idx, )
            heapq.heappush(heap, _tuple)

    return result

def main():
    assert min_fn == determine_sort_order([1, 1, 1, 1, 1, 1, 1, 2])
    assert max_fn ==  determine_sort_order([4, 4, 4, 4, 0])
    assert min_fn == determine_sort_order([1, 1, 2, 2])
    assert max_fn == determine_sort_order([2, 2, -1, -4])
    assert max_fn == determine_sort_order([-4, -5, -6, -8])
    assert min_fn == determine_sort_order([-8, -6, -4, -1])

    assert [1, 2, 3, 4, 5] == merge_sorted_arrays([1, 3, 4], [2, 5], min_fn)
    assert [5, 4, 3, 2, 2, 1, 1] == merge_sorted_arrays([4, 3, 2, 1], [5, 2, 1], max_fn)

    K = 5
    lst_of_sorted_arrays = [sorted([random.randint(-1000, 10000) for _ in range(10)]) for _ in range(K)]
    temp = []
    for lst in lst_of_sorted_arrays:
        temp += lst
    assert sorted(temp) == merge_k_sorted_arrays(lst_of_sorted_arrays, K)

    K = 5
    lst_of_sorted_arrays = [sorted([random.randint(-1000, 10000) for _ in range(10)], reverse=True) for _ in range(K)]
    temp = []
    for lst in lst_of_sorted_arrays:
        temp += lst
    assert (sorted(temp, reverse=True)) == merge_k_sorted_arrays(lst_of_sorted_arrays, K)

    lst_of_sorted_arrays = [sorted([random.randint(-1000, 10000) for _ in range(10)]) for _ in range(K)]
    temp = []
    #lst_of_sorted_arrays = [[1, 3, 5, 6, 10, 11], [2, 4, 5, 8, 10, 12, 13, 14], [3, 6, 9, 12, 15, 18]]
    K = len(lst_of_sorted_arrays)
    for lst in lst_of_sorted_arrays:
        temp += lst

    assert sorted(temp) == merge_k_sorted_arrays_using_heap(lst_of_sorted_arrays, K)

if __name__ == '__main__':
    main()