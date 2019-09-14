import random

from bst import Node
from bst import Tree as BST


def balanced_bst_from_sorted_array(arr, start, end):
    if start > end:
        return

    mid = (start + end) / 2
    root = Node(arr[mid])
    root.left = balanced_bst_from_sorted_array(arr, start, mid - 1)
    root.right = balanced_bst_from_sorted_array(arr, mid + 1, end)
    return root


def main():
    N = 22
    arr = sorted([random.randint(1, N * N) for _ in range(N)])
    print arr
    root = balanced_bst_from_sorted_array(arr, 0, len(arr) - 1)
    tree = BST()
    tree.root = root
    tree.pretty_print()

    inorder = [node.key for node in tree.inorder_nodes()]
    assert arr == inorder


if __name__ == '__main__':
    main()
