"""
Implement an inorder traversal iterator
"""

import random

from bst import Tree as BST


class InorderIterator:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.__push_all_left_children(self.root)

    def next(self):
        node = self.stack.pop()
        self.__push_all_left_children(node.right)
        return node

    def has_next(self):
        return len(self.stack) != 0

    def __push_all_left_children(self, node):
        """
        pushes the current node and all of it's left children on the stack
        """
        while node:
            self.stack.append(node)
            node = node.left


def inorder(node, result):
    if not node:
        return

    inorder(node.left, result)
    result.append(node.key)
    inorder(node.right, result)


def reverse_order(node, result):
    if not node:
        return

    reverse_order(node.right, result)
    result.append(node.key)
    reverse_order(node.left, result)


def main():
    tree = BST()
    N = 10
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "hello")

    inorder_result = []
    inorder(tree.root, inorder_result)

    iterator_result = []
    iterator = InorderIterator(tree.root)
    while iterator.has_next():
        iterator_result.append(iterator.next().key)
    assert inorder_result == iterator_result


if __name__ == '__main__':
    main()
