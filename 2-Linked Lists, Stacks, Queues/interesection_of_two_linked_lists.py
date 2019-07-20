"""
Given two singly linked lists L1 and L2 containing non-negative integers, you have to
find the intersection of given linked lists if any.

Intersection of two linked lists is the first common node (first node with the same address).

Approach:
         Find the lengths of two lists
         Find the difference between their lengths
         Advance a pointer in to longer list by the difference
         Now move two pointers in both lists at the same time and see if they both point to same node
"""

from doubly_linked_list import DoublyList, Node

def size(lst):
    cnt = 0
    current = lst.head
    while current:
        cnt += 1
        current = current.next
    return cnt

def common_node(lst1, lst2):
    size1 = size(lst1)
    size2 = size(lst2)
    longer_lst = shorter_lst = None

    if size1 > size2:
        longer_lst = lst1
        shorter_lst = lst2
    else:
        longer_lst = lst2
        shorter_lst = lst1

    current_longer = longer_lst.head
    current_shorter = shorter_lst.head

    for _ in range(abs(size1-size2)):
        current_longer = current_longer.next

    while current_longer and current_shorter:
        if current_longer is current_shorter:
            return current_longer

        current_longer = current_longer.next
        current_shorter = current_shorter.next

    return None


def main():
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst1 = DoublyList()
    common = None
    for idx, n in enumerate(numbers1):
        node = Node(n, "hello:%d" % n)
        lst1.add_node(node)
        if idx == 5:
            common = node

    lst2 = DoublyList()
    numbers2 = [13, 14, 15]
    for idx, n in enumerate(numbers2):
        lst2.add(n, "hello:%d" % n)

    # join them
    lst2.tail.next = common
    lst2.tail = lst1.tail

    assert common == common_node(lst1, lst2)

    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst1 = DoublyList()
    for idx, n in enumerate(numbers1):
        node = Node(n, "hello:%d" % n)
        lst1.add_node(node)

    lst2 = DoublyList()
    numbers2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for idx, n in enumerate(numbers2):
        lst2.add(n, "hello:%d" % n)

    assert None is common_node(lst1, lst2)

if __name__ == '__main__':
    main()