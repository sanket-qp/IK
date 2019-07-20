import random
from doubly_linked_list import DoublyList

def unflatten_list(lst):
    slow = lst.head
    fast = lst.head.next if lst.head else lst.head
    while slow and (slow is not fast):
        print "slow: %s, fast: %s" % (slow, fast)
        if not slow.child:
            slow = slow.next

        if fast and (fast.next is slow.child):
            temp = fast
            fast = fast.next
            slow = slow.next
            temp.next = None

        elif fast:
            fast = fast.next


def flatten_list(lst):
    slow = lst.head
    fast = lst.head.next if lst.head else lst.head
    while slow and (slow is not fast):
        if not slow.child:
            slow = slow.next

        if fast.next:
            fast = fast.next
        else:
            fast.next = slow.child
            slow = slow.next

def main():
    list1 = DoublyList()
    list1.add(5, "hello5")
    list1.add(33, "hello33")
    list1.add(17, "hello17")
    list1.add(2, "hello2")
    list1.add(1, "hello1")

    list2_1 = DoublyList()
    list2_1.add(6, "hello6")
    list2_1.add(25, "hello25")
    list2_1.add(6, "hello6")

    list2_2 = DoublyList()
    list2_2.add(2, "hello2")
    list2_2.add(7, "hello7")

    list3_1 = DoublyList()
    list3_1.add(8, "hello8")

    list3_2 = DoublyList()
    list3_2.add(9, "hello9")

    list3_3 = DoublyList()
    list3_3.add(12, "hello12")
    list3_3.add(5, "hello5")

    list4 = DoublyList()
    list4.add(7, "hello7")

    list5 = DoublyList()
    list5.add(21, "hello21")
    list5.add(3, "hello3")

    # connect to child lists
    list1.head.child = list2_1.head
    list1.tail.prev.prev.child = list2_2.head
    list2_1.head.next.child = list3_1.head
    list2_1.tail.child = list3_2.head
    list2_2.head.child = list3_3.head
    list3_2.head.child = list4.head
    list3_3.head.child = list5.head

    # flatten the list now
    flatten_list(list1)
    flattened = []
    current = list1.head
    while current:
        flattened.append(current.key)
        current = current.next

    assert [5, 33, 17, 2, 1, 6, 25, 6, 2, 7, 8, 9, 12, 5, 7, 21, 3] == flattened

    # unflatten the list now
    unflatten_list(list1)
    unflattened = []
    current = list1.head
    while current:
        unflattened.append(current.key)
        current = current.next

    assert [5, 33, 17, 2, 1] == unflattened

if __name__ == '__main__':
    main()