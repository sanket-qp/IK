"""
Given an infinite stream of numbers, print K largest numbers encountered so far when the number 404 is encountered
k_largest_numbers(3) = [100, 400, 200, 300, 20, 10, 500, 404, 1000, 50] => [300, 400, 500]

Approach:
    keep a min heap of size K
    keep adding numbers to the heap
    check if the current number from the stream is bigger than minimum number in heap
        then remove the minimum from heap and add the current number to the heap
"""

import random
from heap_sort import Heap

def extract_k_largest(heap):
    retrieved = []
    while not heap.empty():
        retrieved.append(heap.remove())
    for element in retrieved:
        heap.add(element)
    return retrieved

def k_largest_numbers(arr, k, SPECIAL_NUMBER):
    heap = Heap()
    for idx, current_element in enumerate(arr):
        if (current_element == SPECIAL_NUMBER):
            lst = extract_k_largest(heap)
            print "%s" % lst
            print "-------------------------------------"
        elif idx < k:
            heap.add(current_element)
        elif heap.top_element() < current_element:
            heap.remove()
            heap.add(current_element)

def main():
    SPECIAL_NUMBER = 404
    K = 3
    numbers = [random.randint(0, 100) for _ in range(20)]
    # insert 404 at random places in this array
    for _ in range(3):
        random_idx = random.randint(1, len(numbers))
        numbers.insert(random_idx, SPECIAL_NUMBER)

    #numbers = [38, 1, 44, 81, 35, 1, 51, 88, 25, 40, 404, 99, 98, 72, 404, 1, 18, 80, 93, 404, 78, 98, 60]
    print "original numbers: %s" % numbers
    k_largest_numbers(numbers, K, SPECIAL_NUMBER)

if __name__ == '__main__':
    main()

