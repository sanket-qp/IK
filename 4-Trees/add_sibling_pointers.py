"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
"""

from bst import Node
from bst import Tree as BST


def add_sibling_pointers(root):
    def connect(left, right):
        if not left:
            return

        left.next = right
        connect(left.left, left.right)
        connect(left.right, right.left)
        connect(right.left, right.right)

    if not root or not root.left:
        return root
    connect(root.left, root.right)
    return root


def main():
    complete_binary_tree = BST()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    complete_binary_tree.root = one
    add_sibling_pointers(complete_binary_tree.root)
    nodes = list(complete_binary_tree.levelorder_nodes())

    # verify the next pointers
    assert one.next is None
    assert two.next is three
    assert three.next is None
    assert four.next is five
    assert five.next is six
    assert six.next is seven
    assert seven.next is None


if __name__ == '__main__':
    main()
