import random

from bst import Tree as BST


class PostorderIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.__push__all_right_childeren(self.root)

    def __push__all_right_childeren(self, node):
        while node:
            self.stack.append(node)
            node = node.right

    def next(self):
        node = self.stack.pop()
        self.__push__all_right_childeren(node.left)
        return node

    def has_next(self):
        return len(self.stack) != 0


def main():
    tree = BST()
    N = 10
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "")

    tree.pretty_print()
    postorder = [node.key for node in tree.postorder_nodes()]
    print postorder
    postorder_iterator = PostorderIterator(tree.root)
    idx = 0
    while postorder_iterator.has_next():
        postorder_iterator.next() is postorder[idx]
        idx += 1


if __name__ == '__main__':
    main()
