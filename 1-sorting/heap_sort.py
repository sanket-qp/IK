"""
heap sort implementation
"""
import random
import numpy

class Array:
    def __init__(self, initial_size = 10, numbers = []):
        self.arr = numpy.empty((initial_size,), int) if not numbers else numpy.array(numbers)
        self.total_elements = len(numbers) if numbers else 0

    def add(self, index, element):
        if self.total_elements == len(self.arr):
            self.__double_the_capacity()

        self.arr[self.total_elements] = element
        self.total_elements += 1

    def add_last(self, element):
        self.add(self.total_elements, element)

    def element_at_index(self, index):
        if index <0 or index >= self.total_elements:
            raise Exception("array index out of bound")

        return self.arr[index]

    def remove(self, index):
        if index >= self.total_elements:
            raise Exception("array index out of bound")

        element = self.arr[index]
        self.arr[index] = -1
        self.total_elements -= 1
        return element

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.total_elements-1)

    def first_element(self):
        return self.arr[0]

    def move_last_to_first(self):
        self.arr[0] = self.arr[self.total_elements-1]
        self.remove(self.total_elements-1)

    def size(self):
        return self.total_elements;

    def __getitem__(self, idx):
        return self.element_at_index(idx)

    def __setitem__(self, idx, element):
        self.arr[idx] = element

    def __double_the_capacity(self):
        new_size = self.total_elements * 2
        new_arr = numpy.empty((new_size,), int)
        for idx, element in enumerate(self.arr):
            new_arr[idx] = element
        self.arr = new_arr

    def __str__(self):
        return "{[total_elements: %s][%s]}" % (self.total_elements, [self.arr[x] for x in range(self.total_elements)])

class Heap:
    def __init__(self):
        self.arr = Array(initial_size=1)

    def add(self, element):
        self.arr.add_last(element)
        last_element_idx = self.arr.size()-1
        self.__trickle_up(last_element_idx)

    def remove(self):
        # remove the first element, which should be be smallest
        element = self.arr.first_element()
        # move the last element to the first element
        self.arr.move_last_to_first()
        # trickle it down to proper index
        if self.arr.size() > 0:
            self.__trickle_down(0)

        self.arr[self.arr.size()] = element
        return element

    def top_element(self):
        return self.arr.first_element()

    def empty(self):
        return self.arr.size() == 0

    def __trickle_up(self, from_idx):
        child_idx = from_idx
        while True:
            parent_idx = self.__parent_index(child_idx)

            if child_idx <0 or parent_idx < 0:
                break

            child_value = self.arr[child_idx]
            parent_value = self.arr[parent_idx]

            if parent_value < child_value:
                break

            self.arr[child_idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[child_idx]
            child_idx = parent_idx

    def __trickle_down(self, from_idx):
        parent_idx = from_idx
        while True:
            smaller_child_idx = self.__smaller_child_idx(parent_idx)

            if not smaller_child_idx:
                break

            if smaller_child_idx > self.arr.size()-1 or parent_idx > self.arr.size()-1:
                break

            parent_value = self.arr[parent_idx]
            child_value = self.arr[smaller_child_idx]
            if (child_value > parent_value):
                break

            # swap the parent with a smaller child
            self.arr[parent_idx], self.arr[smaller_child_idx] = self.arr[smaller_child_idx], self.arr[parent_idx]
            parent_idx = smaller_child_idx

    def __parent_index(self, child_idx):
        return (child_idx - 1)/2

    def __child_indices(self, parent_idx):
        return 2*parent_idx + 1, 2*parent_idx + 2

    def __smaller_child_idx(self, parent_idx):
        left_child_idx, right_child_idx = self.__child_indices(parent_idx)

        if left_child_idx >= self.arr.size():
            return None

        if right_child_idx >= self.arr.size():
            return left_child_idx

        smaller_idx = left_child_idx if self.arr[left_child_idx] < self.arr[right_child_idx] else right_child_idx
        return smaller_idx

    def __heapify(self):
        start_idx = 0
        end_idx = self.arr.size()/2
        # principal here is, if left tree is a heap and right tree also is a heap then to make a parent element a valid heap,
        # simple go to each element and trickle it down to proper index
        while end_idx >= start_idx:
            self.__trickle_down(end_idx)
            end_idx -= 1

    @staticmethod
    def from_array(lst):
        heap = Heap()
        heap.arr = Array(numbers=lst)
        heap.__heapify()
        return heap

    def __str__(self):
        return "%s" % self.arr


def __heapify(arr, current_idx):
    if current_idx < 0 or current_idx >= len(arr):
        return

    left_child_idx, right_child_idx = 2 * current_idx + 1, 2 * current_idx + 2
    __heapify(arr, left_child_idx)
    __heapify(arr, right_child_idx)

    print current_idx, left_child_idx, right_child_idx
    # swap parent with the smaller child
    if left_child_idx < 0 or left_child_idx >= len(arr):
        return

    if right_child_idx >= len(arr):
        smaller_idx = left_child_idx
    else:
        smaller_idx = left_child_idx if arr[left_child_idx] < arr[right_child_idx] else right_child_idx

    print "parent:%d, left_child:%d, right_child:%d, smaller_child:%d" % (arr[current_idx], arr[left_child_idx], arr[right_child_idx], arr[smaller_idx])
    if (arr[smaller_idx] < arr[current_idx]):
        print "swaping %d with %d" % (arr[current_idx], arr[smaller_idx])
        arr[current_idx], arr[smaller_idx] = arr[smaller_idx], arr[current_idx]
        print arr
    print "---------------------------------------------------------------"

def heapify(arr):
    return __heapify(arr, 0)

def main():
    arr = Array(initial_size=10)
    lst = [random.randint(0, 100) for _ in range(40)]
    for idx, element in enumerate(lst):
        arr.add(idx, element)

    assert arr.size() == len(lst)
    assert lst[4] == arr.element_at_index(4)
    assert lst[-1] == arr.element_at_index(len(lst)-1)

    arr.remove(0)
    assert arr.size() == len(lst)-1


    heap = Heap()
    arr = [random.randint(0, 100) for _ in range(10)]
    for element in arr:
        heap.add(element)

    retrived = []
    while not heap.empty():
        removed = heap.remove();
        retrived.append(removed)
    assert retrived == sorted(arr)

    # arr = [57, 18, 10, 71, 27, 13, 28, 83, 2]
    arr = [random.randint(0, 100) for _ in range(10)]
    heap = Heap.from_array(arr)
    retrived = []
    while not heap.empty():
        removed = heap.remove();
        retrived.append(removed)
    assert retrived == sorted(arr)


if __name__ == '__main__':
    main()