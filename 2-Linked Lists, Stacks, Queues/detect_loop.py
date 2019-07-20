import random
from doubly_linked_list import DoublyList


def detect_loop(lst):
    fast = lst.head
    slow = lst.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # print "fast:%s, slow:%s" % (fast, slow)
        if fast is slow:
            return True
    return False


def length_of_loop(lst):
    fast = lst.head
    slow = lst.head

    nodes_in_loop = 1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # print "fast:%s, slow:%s" % (fast, slow)
        if fast is slow:
            # let's stop incrementing fast and increment slow until it meets fast again
            slow = slow.next
            while slow is not fast:
                nodes_in_loop += 1
                slow = slow.next
            return nodes_in_loop
    return nodes_in_loop

def start_of_loop(lst):
    """
    Approach: we'll find the legnth of the loop, we'll advance one pointer to up to loop length and will advance both pointers in lock step after this point,
    Whenever they meet, is a start of the loop
    """
    loop_length = length_of_loop(lst)
    first = lst.head
    second = lst.head

    # move the fist pointer up to loop length:
    for _ in range(loop_length):
        first = first.next
        print "first :%s" % first

    print "---------------"
    while first is not second:
        print "first :%s" % first
        print "second: %s" % second
        second = second.next
        first = first.next

    return second

def main():

    N = 10
    _input = [random.randint(1, 10) for _ in range(N)]
    print _input
    lst = DoublyList()
    for key in _input:
        data = "hello:%s" % key
        lst.add(key, data)

    assert False is detect_loop(lst)

    # go to last node and connect it with second node
    current = lst.head
    while current:
        temp = current
        current = current.next

    last_node = temp
    second_node = lst.head
    for _ in range(1):
        second_node = second_node.next

    last_node.next = second_node
    loop_present = detect_loop(lst)
    assert True is loop_present

    print "2nd node: %s" % second_node

    if loop_present:
        loop_length = length_of_loop(lst)
        print "length:%d" % loop_length
        assert N-1 == loop_length
        loop_start = start_of_loop(lst)
        assert second_node is loop_start

if __name__ == '__main__':
    main()