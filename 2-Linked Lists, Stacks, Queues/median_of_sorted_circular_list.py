"""
Given a pointer ptr to an arbitrary node of a sorted circular singly linked list L,
having n nodes, containing only even integers, you have to find the median value M of L.

When n is an even number, then the median M is average of two middle elements in a sequence of elements in L, arranged in sorted order.
"""
import random
from doubly_linked_list import DoublyList, Node

ASC_ORDER = 0
DESC_ORDER = 1

def middle(lst, frm, _to):
    slow = lst.head
    fast = lst.head

    slow = frm
    fast = frm
    prev = slow

    while True:
        prev = slow
        slow = slow.next
        fast = fast.next.next

        if fast is frm:
            break

        if fast.next is frm:
            slow = slow.next
            break

    return prev, slow


def get_order(node1, node2):
    if node1 <= node2:
        return ASC_ORDER
    else:
        return DESC_ORDER

def median(sorted_lst, node):
    print "RANDOM NODE: %s" % node
    prev = node
    current = node.next
    size = 1
    start_node = end_node = None
    order_changed = False
    start_found = False
    prev_order = get_order(prev, current)

    while True:
        print "---------------------"
        print "prev: %s, current: %s, order: %s" % (prev, current, prev_order)
        size += 1
        current_order = get_order(prev, current)
        order_changed = True if prev_order != current_order else False
        #print "order changed: %s" % order_changed

        if order_changed and not start_found:
            start_found = True
            if current_order == ASC_ORDER:
                start_node = prev
                end_node = current
            else:
                start_node = current
                end_node = prev

        prev = current
        current = current.next
        prev_order = current_order
        if current is node:
            break

    print "start", start_node
    print "end", end_node

    prev, mid = middle(sorted_lst, start_node, end_node)
    print "MID: %s, PREV: %s, SIZE: %d, NEXT: %s, SUM: %d" % (mid, prev, size, mid.next, (mid.key + prev.key))
    print "HELLO: %d" % (((mid.key + prev.key)/2.0))
    if size % 2 == 0:
        return (mid.key + prev.key)/2.0
    else:
        return mid.key

def median_of_list(lst):
    length = len(lst)
    print "LENGTH", length
    mid_idx = (length-1)//2
    print "MID", mid_idx
    print "MID: %d, NEXT: %d, sum: %d" % (lst[mid_idx], lst[mid_idx+1], (lst[mid_idx] + lst[mid_idx+1]))
    print "HELLO2: %d" % ((lst[mid_idx+1] + lst[mid_idx])/2)
    return lst[mid_idx] if length % 2 != 0 else (lst[mid_idx+1] + lst[mid_idx])/2.0

def main():
    N = 10
    random_idx = random.randint(1, N-1)
    #random_idx = 0
    numbers = [1,2,3,4,5,6,7,8,9,10]
    expected_median = 5.5
    sorted_lst = DoublyList()
    random_node = None
    for idx, n in enumerate(numbers):
        node = Node(n, "hello:%d" % n)
        sorted_lst.add_node(node)

        if random_idx == idx:
            random_node = node

    # make it circular
    sorted_lst.tail.next = sorted_lst.head
    print numbers
    actual_median = median(sorted_lst, random_node)
    print "EXPECTED: %f, ACTUAL: %f" % (expected_median, actual_median)
    assert expected_median == actual_median

    # -----------------------------------------------------------------------------------------------

    N = 11
    random_idx = random.randint(1, N-1)
    numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected_median = 6
    sorted_lst = DoublyList()
    random_node = None
    for idx, n in enumerate(numbers):
        node = Node(n, "hello:%d" % n)
        sorted_lst.add_node(node)

        if random_idx == idx:
            random_node = node

    # make it circular
    sorted_lst.tail.next = sorted_lst.head
    print numbers
    actual_median = median(sorted_lst, random_node)
    print "EXPECTED: %f, ACTUAL: %f" % (expected_median, actual_median)
    assert expected_median == actual_median

    # -----------------------------------------------------------------------------------------------

    N = 11
    random_idx = random.randint(1, N - 1)
    numbers = [3, 2, 1, 11, 10, 9, 8, 7, 6, 5, 4]
    numbers = [6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5]
    expected_median = 6
    sorted_lst = DoublyList()
    random_node = None
    for idx, n in enumerate(numbers):
        node = Node(n, "hello:%d" % n)
        sorted_lst.add_node(node)

        if random_idx == idx:
            random_node = node

    # make it circular
    sorted_lst.tail.next = sorted_lst.head
    print numbers
    actual_median = median(sorted_lst, random_node)
    print "EXPECTED: %f, ACTUAL: %f" % (expected_median, actual_median)
    assert expected_median == actual_median

    # -----------------------------------------------------------------------------------------------

    N = 10
    random_idx = random.randint(1, N - 1)
    numbers = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    expected_median = 5.5
    sorted_lst = DoublyList()
    random_node = None
    for idx, n in enumerate(numbers):
        node = Node(n, "hello:%d" % n)
        sorted_lst.add_node(node)

        if random_idx == idx:
            random_node = node

    # make it circular
    sorted_lst.tail.next = sorted_lst.head
    print numbers
    actual_median = median(sorted_lst, random_node)
    print "EXPECTED: %f, ACTUAL: %f" % (expected_median, actual_median)
    assert expected_median == actual_median


if __name__ == '__main__':
    main()