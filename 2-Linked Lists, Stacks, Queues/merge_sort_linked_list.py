"""
You are given a singly linked list. You have to sort the linked list using merge sort algorithm in ascending order.
"""

import random
from doubly_linked_list import DoublyList, Node

def middle(lst, _from, _to):
    slow = _from
    fast = _from
    while fast and fast.next:
        if fast is _to or fast.next is _to:
            break

        slow = slow.next
        fast = fast.next.next
    return slow

def merge(lst1, lst2):
    current1 = lst1.head
    current2 = lst2.head
    new_list = DoublyList()
    while current1 and current2:
        if current1 < current2:
            new_list.add_node(current1)
            current1 = current1.next
        else:
            new_list.add_node(current2)
            current2 = current2.next


    while current1:
        new_list.add_node(current1)
        current1 = current1.next

    while current2:
        new_list.add_node(current2)
        current2 = current2.next

    return new_list

def __merge_sort(lst, frm, _to):

    if frm is _to:
        new_lst = DoublyList()
        new_node = Node.from_another_node(frm)
        new_lst.add_node(new_node)
        return new_lst

    mid = middle(lst, frm, _to)
    left = __merge_sort(lst, frm, mid)
    right = __merge_sort(lst, mid.next, _to)
    return merge(left, right)


def merge_sort(lst):
    return __merge_sort(lst, lst.head, lst.tail)

def main():
    N = 10
    numbers = [random.randint(0, 10) for _ in range(N)]
    lst = DoublyList()
    for n in numbers:
        lst.add(n, "hello:%d" % n)


    lst1 = DoublyList()
    lst1.add(1, "hello")
    lst1.add(3, "hello")
    lst1.add(5, "hello")
    lst1.add(7, "hello")

    lst2 = DoublyList()
    lst2.add(2, "hello")
    lst2.add(4, "hello")
    lst2.add(6, "hello")
    lst2.add(8, "hello")

    expected = [1,2,3,4,5,6,7,8]
    new_list = merge(lst1, lst2)
    actual = new_list.keys()
    assert expected == actual

    sorted_list = merge_sort(lst)
    actual = sorted_list.keys()

    print "original: %s" % numbers
    print "sorted: %s" % actual
    assert actual == sorted(numbers)

if __name__ == '__main__':
    main()