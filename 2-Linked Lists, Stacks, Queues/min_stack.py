"""
Implement a stack which also offers an API called get_min which returns the minimum object at any given time in the stack
"""
import sys
import random

class Stack:

    def __init__(self):
        self.lst = []
        self.min_so_far = sys.maxint

    def push(self, item):
        if item < self.min_so_far:
            self.min_so_far = item
        self.lst.append((item, self.min_so_far, ))

    def pop(self):
        item, min_so_far = self.lst.pop(-1)
        # update the min_so_far
        if not self.empty():
            self.min_so_far = self.get_min()
        else:
            self.min_so_far = sys.maxint
        return item

    def peek(self):
        item, min_so_far = self.lst[-1]
        return item

    def count(self):
        return len(self.lst)

    def get_min(self):
        top_item, min_so_far = self.lst[-1]
        return min_so_far

    def empty(self):
        return len(self.lst) == 0

    def __str__(self):
        return "%s" % self.lst


def main():
    N = 10
    numbers = [random.randint(0, 10) for _ in range(N)]
    stack = Stack()
    for n in numbers:
        stack.push(n)

    popped = []
    while not stack.empty():
        item = stack.pop()
        popped.append(item)

    assert popped == list(reversed(numbers))

    numbers = [10, 9, 8, 7, 6]
    for n in numbers:
        stack.push(n)

    idx = len(numbers)-1
    while not stack.empty():
        _min, item = stack.min_so_far, stack.pop()
        assert _min == numbers[idx]
        assert item == numbers[idx]
        idx -= 1

    numbers = [-1, 10, 20, -2, 5, 4]
    for n in numbers:
        stack.push(n)

    _min, item = stack.min_so_far, stack.pop()
    assert -2 == _min
    assert 4 == item

    _min, item = stack.min_so_far, stack.pop()
    assert -2 == _min
    assert 5 == item

    _min, item = stack.min_so_far, stack.pop()
    assert -2 == _min
    assert -2 == item

    _min, item = stack.min_so_far, stack.pop()
    assert -1 == _min
    assert 20 == item

    _min, item = stack.min_so_far, stack.pop()
    assert -1 == _min
    assert 10 == item

    _min, item = stack.min_so_far, stack.pop()
    assert -1 == _min
    assert -1 == item

    assert True is stack.empty()

if __name__ == '__main__':
    main()