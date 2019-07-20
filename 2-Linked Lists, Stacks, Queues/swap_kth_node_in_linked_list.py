"""
Given an integer singly linked list L of size n, and an integer k,
you have to swap kth (1-indexed) node from the beginning, with kth node from the end.
Note that you have to swap the nodes themselves, not just the contents.

Constraints:
    Try to access linked list nodes minimum number of times.


Approach: keep 2 pointers
          Advance first pointer to K nodes
          Then Start second pointer from the begining of the list and Advance both pointer until the first pointer reaches the end
          At this point, 2nd pointer will point to the Kth node from the right
"""

import random
from doubly_linked_list import DoublyList

def xswap_kth_nodes(lst, K):
    # add all the elements on a stack
    stack = []
    current = lst.head
    prev = None
    idx = 1

    kth_node_left = None
    kth_node_left_parent = None

    kth_node_right = None
    kth_node_right_parent = None

    while current:
        if idx == K:
            kth_node_left = current
            kth_node_left_parent = prev
        stack.append(current)
        prev = current
        current = current.next
        idx += 1

    # now pop from stack to get the Kth node from right
    idx = 1
    while stack:
        current = stack.pop()
        if idx == K:
            kth_node_right = current

        if idx == K + 1:
            kth_node_right_parent = current

        idx += 1

    # swap them
    # special cases
    if K == 1:
        temp_left = kth_node_left.next
        temp_right = None
        lst.head = kth_node_right
        kth_node_right.next = temp_left

        kth_node_right_parent.next = kth_node_left
        kth_node_left.next = temp_right

    elif kth_node_left.next is kth_node_right:
        temp_right = kth_node_right.next
        kth_node_left_parent.next = kth_node_right
        kth_node_right.next = kth_node_left
        kth_node_left.next = temp_right
    else:

        temp_left = kth_node_left.next
        temp_right = kth_node_right.next

        kth_node_left_parent.next = kth_node_right
        kth_node_right.next = temp_left

        kth_node_right_parent.next = kth_node_left
        kth_node_left.next = temp_right

def swap_kth_nodes(lst, K):
    ptr1 = ptr2 = lst.head
    kth_node_left = None
    kth_node_left_parent = None
    kth_node_right = None
    kth_node_right_parent = None
    current = lst.head
    prev = None
    idx = 1
    while idx <= K:
        if idx == K:
            kth_node_left = ptr1
            kth_node_left_parent = prev


        prev = ptr1
        ptr1 = ptr1.next
        idx += 1

    while ptr1:
        prev = ptr2
        ptr2 = ptr2.next
        ptr1 = ptr1.next

    kth_node_right = ptr2
    kth_node_right_parent = prev

    # swap them
    # special cases
    if K == 1:
        temp_left = kth_node_left.next
        temp_right = None
        lst.head = kth_node_right
        kth_node_right.next = temp_left

        kth_node_right_parent.next = kth_node_left
        kth_node_left.next = temp_right

    elif kth_node_left.next is kth_node_right:
        temp_right = kth_node_right.next
        kth_node_left_parent.next = kth_node_right
        kth_node_right.next = kth_node_left
        kth_node_left.next = temp_right
    else:

        temp_left = kth_node_left.next
        temp_right = kth_node_right.next

        kth_node_left_parent.next = kth_node_right
        kth_node_right.next = temp_left

        kth_node_right_parent.next = kth_node_left
        kth_node_left.next = temp_right

def main():
    N = 20
    K = random.randint(0, 10)
    print K
    numbers = [random.randint(1, 10) for _ in range(N)]
    expected = numbers[:]
    expected[K-1], expected[N-K] = expected[N-K], expected[K-1]
    print numbers
    lst = DoublyList()
    for key in numbers:
        data = "hello:%s" % key
        lst.add(key, data)

    swap_kth_nodes(lst, K)

    actual = []
    current = lst.head
    while current:
        actual.append(current.key)
        current = current.next
    assert expected == actual
    print actual


if __name__ == '__main__':
    main()