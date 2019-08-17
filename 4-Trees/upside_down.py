"""
Given a binary tree where every node has either 0 or 2 children
and every right node is a leaf node,

flip it upside down turning it into a binary tree where all left nodes are leafs.
"""
from bst import Node
from bst import Tree


def traverse_left(root, parent, d):
    if not root:
        return

    traverse_left(root.left, root, d)
    if 'root' not in d:
        d['root'] = root

    root.right = parent
    if parent:
        root.left = parent.right
    else:
        root.left = None


def upside_down(tree):
    d = {}
    traverse_left(tree.root, None, d)

    inverted = Tree()
    inverted.root = d['root']
    return inverted


def main():
    one = Node(1, "")
    two = Node(2, "")
    three = Node(3, "")
    four = Node(4, "")
    five = Node(5, "")
    six = Node(6, "")
    seven = Node(7, "")
    eight = Node(8, "")
    nine = Node(9, "")

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    four.left = six
    four.right = seven

    tree = Tree()
    tree.root = one
    tree.levelorder()
    inverted = upside_down(tree)
    inverted.levelorder()


if __name__ == '__main__':
    main()
