"""
An integer array named arr is given to you. Size of arr is n and assume that it is very large.
There is a sliding window of size w, which is moving from the very left of the array to the very right.
You can only see the w numbers in the window.
Each time the sliding window moves rightwards by one position.
You have to find maximum number in the window each time.
"""
import sys
import heapq
import random

class MaxHeap:
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.current_size = 0
        self.heap = []
        self.min_index = 0
        self.min_element = sys.maxint

    def add(self, element):
        # multiply by -1 for max heap
        if len(self.heap) >= self.heap_size:
            self.remove_min()

        heapq.heappush(self.heap, -1 * element)

    def remove_min(self):
        # remove the last element, which should be the smallest
        self.heap.pop()

    def pop(self):
        return -1 * heapq.heappop(self.heap)

    def top(self):
        if not self.empty():
            return -1 * self.heap[0]
        return None

    def empty(self):
        return len(self.heap) == 0

    def __str__(self):
        lst = []
        while self.heap:
            lst.append(-1 * heapq.heappop(self.heap))

        for element in lst:
            heapq.heappush(self.heap, element)

        return "%s" % lst


def max_in_sliding_window(arr, window_size):
    start, end = get_start_and_end_index(len(arr), window_size)
    heap = MaxHeap(window_size)
    max_elements = []

    for start in range(0, window_size):
        heap.add(arr[start])

    for idx in range(start+1, len(arr)):
        max_elements.append((idx-window_size, idx-1, heap.top()))
        heap.add(arr[idx])

    print max_elements


def get_start_and_end_index(list_len, window_len):
    return 0, max(0, list_len - window_len)


def main():
    N = 10
    W = 3
    numbers = [random.randint(1, 10) for _ in range(N)]
    numbers = [6, 4, 8, 1, 9, 6, 2, 7, 2, 8]

    assert (0, 6) == get_start_and_end_index(10, 4)
    assert (0, 0) == get_start_and_end_index(4, 4)
    assert (0, 8) == get_start_and_end_index(10, 2)
    assert (0, 9) == get_start_and_end_index(10, 1)
    assert (0, 0) == get_start_and_end_index(5, 6)

    max_in_sliding_window(numbers, W)

if __name__ == '__main__':
    main()