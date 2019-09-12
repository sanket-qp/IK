"""

You are given root node of a binary tree T. You need to modify that tree in place,
transform it into the mirror image of the initial tree T.

https://medium.com/@theodoreyoong/coding-short-inverting-a-binary-tree-in-python-f178e50e4dac

          ______8______
         /             \
        1             __16
                     /
                   10
                     \
                     15

should convert to

          ______8______
         /             \
        16__            1
           \
           10
           /
         15
"""

import random

from bst import Tree as BST


def mirror_image(node):
    if not node:
        return

    left = mirror_image(node.left)
    right = mirror_image(node.right)
    temp_left = left
    node.left = right
    node.right = temp_left
    return node


def main():
    tree = BST()
    N = 6
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "")

    tree.pretty_print()
    mirror_image(tree.root)
    print ""
    print "after inverting"
    tree.pretty_print()


if __name__ == '__main__':
    main()
