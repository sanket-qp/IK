"""
Given an integer singly linked list L, of size n, and an integer k, you have to reverse every k nodes of the linked list.

List = 1 -> 2 -> 3 -> 4 -> 5 -> 6
K = 3
Output = 3 -> 2 -> 1 -> 6 -> 5 -> 4
(1,2,3) (4,5,6)

List = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
K = 3
Output = 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7
(1,2,3) (4,5,6) (7,8)
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

def reverse_in_k_groups(lst, K):
    ptr1 = ptr2 = lst.head
    idx = 1
    head_set = False
    prev = None
    prev_tail = None
    while ptr2:
        if idx % K == 0:
            ptr2 = ptr2.next
            new_head, new_tail = reverse_partial_list(lst, ptr1, ptr2)
            if prev_tail:
                prev_tail.next = new_head
            prev_tail = new_tail
            if not head_set:
                lst.head = new_head
                head_set = True
            ptr1 = ptr2
            new_tail.next = ptr2
        else:
            prev = ptr2
            ptr2 = ptr2.next
        idx += 1
    lst.tail = prev


def main():
    N = 10
    K = random.randint(0, 10)
    K = 3
    print "K = %d" % K
    numbers = [random.randint(1, 10) for _ in range(N)]
    numbers = [1,2,3,4,5,6,7,8,9,10,11]
    expected = [3,2,1,6,5,4,9,8,7,10,11]
    print numbers
    lst = DoublyList()
    for key in numbers:
        data = "hello:%s" % key
        lst.add(key, data)

    reverse_in_k_groups(lst, K)

    actual = []
    current = lst.head
    while current:
        actual.append(current.key)
        current = current.next

    print actual
    assert expected == actual

if __name__ == '__main__':
    main()