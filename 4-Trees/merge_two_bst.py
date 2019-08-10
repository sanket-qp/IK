import random

from bst import Tree as BST


def print_nodes(nodes):
    print [x.key for x in nodes]


def inorder(root, result):
    if not root:
        return

    inorder(root.left, result)
    result.append(root)
    inorder(root.right, result)


def balanced_bst_from_sorted_array(arr, start, end):
    if start > end:
        return

    mid = start + (end - start) / 2
    root = arr[mid]
    root.left = balanced_bst_from_sorted_array(arr, start, mid - 1)
    root.right = balanced_bst_from_sorted_array(arr, mid + 1, end)
    return root


def merge(t1, t2):
    inorder_t1 = []
    inorder_t2 = []

    inorder(t1.root, inorder_t1)
    inorder(t2.root, inorder_t2)

    merged_arr = sorted(inorder_t1 + inorder_t2)
    print_nodes(merged_arr)
    root = balanced_bst_from_sorted_array(merged_arr, 0, len(merged_arr) - 1)

    tree = BST()
    tree.root = root
    return tree


def main():
    t1 = BST()

    N = 5
    arr1 = list(set([random.randint(1, 10) for _ in range(N)]))
    arr2 = list(set([random.randint(1, 10) for _ in range(N)]))
    print arr1
    print arr2

    for e in arr1:
        t1.insert(e, "")

    t2 = BST()
    for e in arr2:
        t2.insert(e, "")

    merged_tree = merge(t1, t2)
    inorder_merged = []
    inorder(merged_tree.root, inorder_merged)
    merged_tree.levelorder()
    assert sorted(arr1 + arr2) == [x.key for x in inorder_merged]


if __name__ == '__main__':
    main()
