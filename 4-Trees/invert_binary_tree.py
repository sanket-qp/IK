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
