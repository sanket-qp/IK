"""
Given two arrays, find if one is a subset of the other
"""
import random

def index_of(element, sorted_arr):
    start = 0
    end = len(sorted_arr) - 1
    while (start <= end):
        # to avoid overflow, better than (start+end)/2
        mid = start + (end - start) / 2
        if element == sorted_arr[mid]:
            return mid
        elif element < sorted_arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

def is_present(element, sorted_arr):
    return index_of(element, sorted_arr) != None

def is_subset_of_using_binary_search(a, b):
    """
    return true if a is any set is a  subset of the other
    approach:
        sort two arrays
        find a smaller array
        do binary search on larger array for each element in smaller array

    time complexity if we were already given sorted arrays smaller_set * log(larger_set)
    """
    # sort two sets
    a = sorted(a)
    b = sorted(b)

    # find the smaller set
    smaller_set = a if len(a) <= len(b) else b
    larger_set = a if len(a) > len(b) else b

    # do a binary search on a larger set for each element of the smaller set
    for element in smaller_set:
        present = is_present(element, larger_set)
        if not present:
            return False
    return True


def is_subset_of_using_walkthrough(a, b):
    """
    return true if a is any set is a  subset of the other
    approach:
        sort two arrays
        find smaller array
        using binary search on first element of smaller array find the index in larger array
        keep two pointers in small and large array and compare elements
    """
    # sort two sets
    a = sorted(a)
    b = sorted(b)

    # find the smaller set
    smaller_set = a if len(a) <= len(b) else b
    larger_set = a if len(a) > len(b) else b

    if len(smaller_set) == 0:
        return True

    first_smaller_element = smaller_set[0]
    index_in_larger_set = index_of(first_smaller_element, larger_set)

    if index_in_larger_set is None:
        return False

    smaller_idx =  1
    larger_idx = index_in_larger_set + 1
    while True:
        if smaller_idx >= len(smaller_set):
            return True
        elif larger_idx >= len(larger_set) and smaller_idx <= len(smaller_set):
            return False

        if (smaller_set[smaller_idx] == larger_set[larger_idx]):
            smaller_idx += 1
            larger_idx += 1
        else:
            larger_idx += 1

def is_subset_of(set1, set2):
    x = is_subset_of_using_binary_search(set1, set2)
    y = is_subset_of_using_walkthrough(set1, set2)
    return x & y

def main():
    set1 = [1,2,3,4,5,6,7,8]
    set2 = [4, 2]
    assert True is is_subset_of(set1, set2)

    set1 = [1, 2, 3, 4, 5, 6, 7, 8]
    set2 = [44, 22]
    assert False is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [91, 90]
    assert True is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = []
    assert True is is_subset_of(set1, set2)

    set1 = []
    set2 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    assert True is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [14, 91]
    assert True is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [1,2,3,4,5,6,7,8,9,10]
    assert False is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [91, 70, 52, 14, 90, 45, 37, 53, 18, 51]
    assert True is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [14, 18, 37, 45, 51, 52, 53, 70, 90, 100]
    assert False is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [14]
    assert True is is_subset_of(set1, set2)

    set1 = [51, 18, 53, 37, 45, 90, 14, 52, 70, 91]
    set2 = [100]
    assert False is is_subset_of(set1, set2)


if __name__ == '__main__':
    main()