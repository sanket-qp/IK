"""
Given an integer singly linked list L of size n, zip it from its two ends.
What does zipping mean?
Given a singly linked list L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
                              1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL
You have to do it in-place i.e. in the same linked list given in input, using only constant extra space.
"""
import random
from doubly_linked_list import DoublyList


def reverse_partial_list(lst, ptr1, ptr2):
    new_tail = prev = ptr1
    current = ptr1.next
    while current is not ptr2:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    new_head = prev
    new_tail.next = None
    return new_head, new_tail

def zip_list(lst):

    # find the middle of the list
    slow = fast = lst.head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # reverse the list from middle to end
    new_head, new_tail = reverse_partial_list(lst, slow, fast)

    # break two lists off
    prev.next = None

    # merge both lists
    ptr1 = lst.head
    ptr2 = new_head
    while ptr2 and ptr2.next:
        ptr1_next = ptr1.next
        ptr2_next = ptr2.next

        ptr1.next = ptr2
        ptr2.next = ptr1_next

        ptr1 = ptr1_next
        ptr2 = ptr2_next

    ptr1.next = ptr2
    lst.tail = ptr2


def main():
    N = 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = [1, 8, 2, 7, 3, 6, 4, 5]
    print numbers
    lst = DoublyList()
    for key in numbers:
        data = "hello:%s" % key
        lst.add(key, data)

    zip_list(lst)

    current = lst.head
    actual = []
    while current:
        actual.append(current.key)
        current = current.next

    print actual
    assert expected == actual


if __name__ == '__main__':
    main()