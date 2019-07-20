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

    while True:
        if fast is _to:
            break
        if fast.next is _to:
            break

        slow = slow.next
        fast = fast.next.next
    return slow


def get_order(node1, node2):
    if node1 <= node2:
        return ASC_ORDER
    else:
        return DESC_ORDER

def median(sorted_lst, node):
    prev = node
    current = node.next
    size = 0
    start_node = end_node = None
    order_changed = False
    start_found = False
    prev_order = get_order(prev, current)

    while True:
        #print "---------------------"
        #print "prev: %s, current: %s, order: %s" % (prev, current, prev_order)
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

    mid = middle(sorted_lst, start_node, end_node)
    print "MID: %s, SIZE: %d" % (mid, size)
    if size % 2 == 0:
        return (mid.key + mid.next.key)/2
    else:
        return mid.key

def median_of_list(lst):
    length = len(lst)
    print "LENGTH", length
    mid_idx = (length-1)//2
    print "MID", mid_idx
    return lst[mid_idx] if length % 2 != 0 else (lst[mid_idx-1] + lst[mid_idx])/2

def main():
    N = 10
    random_node_idx = random.randint(0, N-1)
    random_node_idx = 3
    #random_node_idx = 1
    numbers = sorted([random.randint(-10, 10) for _ in range(N)])
    numbers = [-10, -10, -10, -1, 1, 2, 3, 4, 4, 10]
    # numbers = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #numbers = [4, 3, 2, 1]
    sorted_lst = DoublyList()
    random_node = None
    for idx, n in enumerate(numbers):
        node = Node(n, "hello:%d" % n)
        sorted_lst.add_node(node)
        if idx == random_node_idx:
            random_node = node

    print "Random node", random_node
    # make it circular
    sorted_lst.tail.next = sorted_lst.head

    print numbers
    llm = median(sorted_lst, random_node)
    lm = median_of_list(numbers)
    print "linked list: %d" % llm
    print "list: %d" % lm
    #assert median_of_list(numbers) == median(sorted_lst, random_node)


if __name__ == '__main__':
    main()