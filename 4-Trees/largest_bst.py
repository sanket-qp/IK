"""
Given a binary tree, find the largest Binary Search Tree (BST),
where largest means BST with largest number of nodes in it. The largest BST must include all of its descendants.
"""
import random

from bst import Tree as BST


def largest_bst(root):
    def largest(node):
        if not node:
            return True, 0

        is_left_bst, left_nodes = largest(node.left)
        is_right_bst, right_nodes = largest(node.right)

        # now check if current node/sub-tree is BST
        # both left and right subtrees have to be BSTs
        is_current_bst = is_left_bst and is_right_bst

        # Also, current node's key should be >= left subtree's key and < right subtree's key
        if node.left:
            is_current_bst &= node.left.key <= node.key

        if node.right:
            is_current_bst &= node.right.key > node.key

        # print "node: %s, _min: %s, _max: %s" % (node.key, _min, _max)
        # print "node: %s, is_left_bst: %s, is_right_bst:%s" % (node.key, is_left_bst, is_right_bst)
        # print "node: %s, left_nodes: %s, right_nodes:%s" % (node.key, left_nodes, right_nodes)

        max_nodes = 0
        if is_left_bst and is_right_bst:
            max_nodes = left_nodes + right_nodes
        elif is_left_bst:
            max_nodes = left_nodes
        elif is_right_bst:
            max_nodes = right_nodes

        if is_current_bst:
            max_nodes += 1
        else:
            max_nodes = max(left_nodes, right_nodes)

        # print "node: %s, is_current_bst: %s, rtn:%s" % (node.key, is_current_bst, rtn)
        # print "----"
        return is_current_bst, max_nodes

    _, num_nodes = largest(root)
    return num_nodes


def main():
    tree = BST()
    N = 11
    _set = set([random.randint(1, N * N) for _ in range(N)])
    # _set = [50, 6, 33, 20, 35, 36]
    for x in _set:
        tree.insert(x, "")

    # just set the root to 0 so the full tree is not BST
    tree.root.key = 0
    tree.pretty_print()
    print "largest bst with nodes: %d" % largest_bst(tree.root)


if __name__ == '__main__':
    main()
