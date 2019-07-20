"""
Given an integer singly linked list L, you have to find the middle node of it. L has total
n no. of nodes.
If it has even number of nodes, then consider the second of the middle two nodes as
the middle node.

Constraints:
    Do it in one pass over the linked list.

Approach: use Slow and Fast pointer, Fast pointer is traversing twice as fast as Slow
so when Fast reaches 10, Slow is at 5
        Fast reaches 20, Slow is at 10
        Fast reaches end, Slow is at the middle element
"""
import random
from doubly_linked_list import DoublyList


def get_middle_element(lst):
    slow = fast = lst.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    N = 10
    numbers = [random.randint(1, 10) for _ in range(N)]
    lst = DoublyList()
    for key in numbers:
        data = "hello:%s" % key
        lst.add(key, data)

    middle = get_middle_element(lst)
    assert numbers[N/2] == middle.key


if __name__ == '__main__':
    main()