class Node:
    """
    Node in the Linked List
    """

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None
        self.child = None # added to test flattening the list problem
        self.random = None # added to test cloning a linked list problem

    def __cmp__(self, other):
        if self.key == other.key:
            return 0
        elif self.key < other.key:
            return -1
        else:
            return 1

    def __str__(self):
        return "[(%d, %s)]" % (self.key, self.data)

    @staticmethod
    def hello():
        return "hello world"

    @staticmethod
    def from_another_node(node):
        new_node = Node(node.key, node.data)
        return new_node

class DoublyList:
    """
    Implementation of dobuly linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, data):
        # create new Node
        node = Node(key, data)
        if (not self.head):
            self.head = node
            self.tail = node
        else:
            tail = self.tail
            tail.next = node
            node.prev = tail
            self.tail = node

    def add_node(self, node):
        if (not self.head):
            self.head = node
            self.tail = node
        else:
            tail = self.tail
            tail.next = node
            node.prev = tail
            self.tail = node

    def move_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        elif node == self.head:
            # do nothing
            pass
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

            old_head = self.head
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head

        else:
            # remove the node from the list
            node.prev.next = node.next
            node.next.prev = node.prev
            # make the node head of the list
            old_head = self.head
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head

    def add_to_front(self, key, data):
        node = Node(key, data)
        self.__add_to_front(node)

    def __add_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            old_head = self.head
            self.head = node
            self.head.next = old_head
            old_head.prev = self.head

    def remove_first(self):
        if not self.head:
            return None

        head = self.head
        self.head = head.next
        self.head.prev = None
        return head

    def remove_last(self):
        if not self.tail:
            return None

        tail = self.tail
        new_tail = tail.prev
        self.tail = new_tail
        new_tail.next = None
        return tail

    def traverse(self, reverse=False):
        current = self.tail if reverse else self.head
        while (current):
            yield current
            current = current.prev if reverse else current.next

    def keys(self):
        lst = []
        for node in self.traverse():
            lst.append(node.key)
        return lst

    def __str__(self):
        l = []

        print "Head = %s" % self.head
        print "Tail = %s" % self.tail
        current = self.head

        if not current:
            return "[]"

        while (current):
            l.append("%s" % (current,))
            current = current.next

            if current is self.head:
                break

        return ' --> '.join(l)


def main():
    l = DoublyList()
    l.add(4, "Hello World")
    l.add(44, "How Are You ?")
    l.add(2, "Test")
    l.add(22, "Test 22")
    l.add_to_front(22, "Test 2222")

    print "%s" % l
    for node in l.traverse(True):
        print "%s" % node


if __name__ == "__main__":
    main()