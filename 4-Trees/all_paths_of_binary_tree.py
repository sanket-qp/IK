"""
Given a binary tree, print out all of its root-to-leaf paths one per line.
e.g. for a tree that's


                                    1
                                |       |
                                2       3
                             |    |   |   |
                             4    5   6   7
Print:
1 2 4
1 2 5
1 3 6
1 3 7
"""
import random

from bst import Tree as BST


def print_path(_path):
    print [x.key for x in _path]
    print "-------------------"


def path(node, taken, result):
    if node.is_leaf():
        result.append(taken[:] + [node])
        return

    taken.append(node)
    if node.left:
        path(node.left, taken, result)
    if node.right:
        path(node.right, taken, result)
    taken.pop()


def all_paths(tree):
    result = []
    taken = []
    path(tree.root, taken, result)
    return result


def main():
    tree = BST()
    N = 10
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "hello")

    print _set
    result = all_paths(tree)
    for _path in result:
        print_path(_path)


if __name__ == '__main__':
    main()
