"""
Given a singly LinkedList list of n elements. The data stored in the nodes of the linked
list are the continuous sequence of the integral natural numbers i.e. the head node
stores the integer 1 , then the next node stores the integer 2 , so on and so forth till
the last node of the linked list stores the integer n.

Now, apart the standard next pointer of the linked-list node; there is a special random pointer that may or may not
exists on each node. This random pointer of a node can point to any node of the linked list including itself.

Your task is to clone the LinkedList List in an efficient manner both in terms of time and space.

                    |-----------------------|
Approach:           |                       |
                    |            |-----|    |
                    |            |     |    |
    Original List : 1 --> 2 -->  3 --> 4--> 5 --> 6
                    |           |
                    |-----------|

    (1) for each node in original linked list we'll create a new node and insert in right after the original node

        1 --> (1) --> 2 --> (2) --> 3 --> (3) --> 4 --> (4) --> 5 --> (5) --> 6 --> (6)

    (2) Now we'll go through the list again and will assign random pointers as follows
        if node.random:
            node.next.random = node.random.next

    (3) we'll separate two lists
"""

import random
from doubly_linked_list import DoublyList, Node

def clone_list(lst):

    # step 1
    # append new nodes after existing nodes
    current = lst.head
    while current:
        current_next = current.next
        new_node = Node(current.key, current.data + " :: new")
        current.next = new_node
        new_node.next = current_next
        current = current_next

    # step2
    # assign random pointers
    current = lst.head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next


    # step 3
    # seperate two lists
    new_list = DoublyList()
    new_head = lst.head.next
    new_list.head = new_head

    old = lst.head
    new = new_head
    while old:
        old.next = new.next
        old = old.next
        new.next = old.next if old else None
        new = new.next if new else None
    return new_list


def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,11]
    lst = DoublyList()
    for key in numbers:
        data = "hello:%s" % key
        lst.add(key, data)

    # add random pointers
    node_1 = lst.head
    node_3 = node_1.next.next
    node_4 = node_3.next
    node_5 = node_4.next
    node_6 = node_5.next

    node_1.random = node_3
    node_3.random = node_4
    node_4.random = node_5
    node_5.random = node_1
    node_6.random = node_6

    expected_randoms = []
    current = lst.head
    while current:
        if current.random:
            expected_randoms.append(current.key)
        current = current.next


    new_list = clone_list(lst)
    actual = []
    actual_randoms = []
    current = new_list.head
    while current:
        actual.append(current.key)
        if current.random:
            actual_randoms.append(current.key)
        current = current.next

    assert numbers == actual
    assert expected_randoms == actual_randoms

if __name__ == '__main__':
    main()