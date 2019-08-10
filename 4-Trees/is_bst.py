"""
This is a very well-known interview problem:
Given a Binary Tree, check if it is a Binary Search Tree (BST). A valid BST doesn't have to be complete or balanced.
"""

import random
import sys

from bst import Node
from bst import Tree as BST


def __is_bst(root, _min, _max):
    if not root:
        return True

    # root of each node should be between given _min and _max
    if not (_min < root.key < _max):
        return False

    return __is_bst(root.left, _min, root.key) and __is_bst(root.right, root.key, _max)


def is_bst(root):
    _min = -sys.maxint
    _max = sys.maxint

    # root of each node should be between given _min and _max
    return __is_bst(root, _min, _max)


def main():
    _50 = Node(50, "hello")
    _25 = Node(25, "hello")
    _75 = Node(75, "hello")
    _12 = Node(12, "hello")
    _34 = Node(34, "hello")
    _60 = Node(60, "hello")
    _80 = Node(80, "hello")
    _55 = Node(55, "hello")
    _22 = Node(22, "hello")

    _50.left = _25
    _50.right = _75
    _25.left = _12
    _25.right = _34
    _75.left = _60
    _75.right = _80
    _12.right = _55
    assert False is is_bst(_50)

    _12.right = _22
    assert True is is_bst(_50)

    tree = BST()
    N = 10
    for _ in range(N):
        tree.insert(random.randint(1, 100), "hello")

    assert True is is_bst(tree.root)

    # skewed tree
    tree = BST()
    for n in range(N):
        tree.insert(n, "hello")

    assert True is is_bst(tree.root)

    # skewed tree
    tree = BST()
    for n in range(N, 0, -1):
        tree.insert(n, "hello")

    assert True is is_bst(tree.root)


if __name__ == '__main__':
    main()
