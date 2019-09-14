"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.
"""

import random

from bst import Node
from bst import Tree as BST


def get_element_idx(element, arr):
    for idx, e in enumerate(arr):
        if e == element:
            return idx
    return -1


def get_traversals_for_subtrees(root_key, inorder, preorder):
    # print "BUILD FROM. root_key: %s, inorder: %s, preorder: %s" % (root_key, inorder, preorder)
    inorder_left = preorder_left = []
    inorder_right = preorder_right = []
    # let's inorder of subtrees first
    # elements left to root_key in inorder, creates a left subtree
    idx = get_element_idx(root_key, inorder)
    inorder_left = inorder[:idx]
    # elements right of the root_key in inorder, creates a right subtree
    inorder_right = inorder[idx + 1:]

    # now let's tackle preorder of subtrees
    if not inorder_left:
        preorder_left = []
        preorder_right = preorder[1:]
    else:
        last_element_in_inorder_left = inorder_left[-1]
        idx = get_element_idx(last_element_in_inorder_left, preorder)
        preorder_left = preorder[1: idx + 1]
        preorder_right = preorder[idx + 1:]

    return inorder_left, preorder_left, inorder_right, preorder_right


def binary_tree_from_traversals(preorder, inorder):
    if not preorder:
        return None

    if not inorder:
        return None

    root_key = preorder[0]
    root = Node(root_key)

    inorder_left, preorder_left, inorder_right, preorder_right = get_traversals_for_subtrees(root_key, inorder,
                                                                                             preorder)
    # print "root: %s, inorder_left: %s, preorder_left: %s" % (root_key, inorder_left, preorder_left)
    # print "root: %s, inorder_right: %s, preorder_right: %s" % (root_key, inorder_right, preorder_right)
    # print "------"

    if inorder_left:
        root.left = binary_tree_from_traversals(preorder_left, inorder_left)

    if inorder_right:
        root.right = binary_tree_from_traversals(preorder_right, inorder_right)

    return root


def main():
    tree = BST()
    N = 11
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "")

    print "original tree"
    tree.pretty_print()

    inorder = [node.key for node in tree.inorder_nodes()]
    preorder = [node.key for node in tree.preorder_nodes()]

    # now build a new tree from these traversals
    root = binary_tree_from_traversals(preorder, inorder)
    new_tree = BST()
    new_tree.root = root
    print "reconstructed tree"
    new_tree.pretty_print()

    # verify the correctness
    for orig_node, cloned_node in zip(tree.levelorder_nodes(), new_tree.levelorder_nodes()):
        assert orig_node is not cloned_node
        assert orig_node.key == cloned_node.key


if __name__ == '__main__':
    main()
