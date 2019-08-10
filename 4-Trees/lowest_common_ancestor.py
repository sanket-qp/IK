"""
You are given root of a binary tree T of n nodes.
You are also given references of two nodes a & b.

You need to find the lowest common ancestor of a and b.
Least or lowest common ancestor (LCA) of two nodes is defined as the lowest node in T that has the two nodes as descendants.

For this problem, we allow a node to be an ancestor/descendant of itself.
"""
from bst import Node


def print_path(path):
    print [x.key for x in path]


def _LCA(root, a, b, path, result):
    if not root:
        return

    path.append(root)

    if root is a or root is b:
        print_path(path)
        result.append(path[:])

    _LCA(root.left, a, b, path, result)
    _LCA(root.right, a, b, path, result)
    path.pop()


def find_common(path1, path2):
    smaller, bigger = (path1, path2) if len(path1) < len(path2) else (path2, path1)
    jdx = 0
    last_common = 0
    # iterate through both arrays and find the element where they differ
    # e.g. 1, 2, 5, 9 and 1, 2, 5, 8 differs at last index,
    # so common element is 5
    for idx, e in enumerate(smaller):
        if e == bigger[jdx]:
            jdx += 1
        else:
            break
        last_common = idx

    return smaller[last_common]


def LCA(root, a, b):
    if a is b:
        return a

    path = []
    result = []
    _LCA(root, a, b, path, result)
    return find_common(result[0], result[1])


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

    three.left = six
    three.right = seven

    five.left = eight
    five.right = nine
    assert five is LCA(one, eight, nine)
    assert two is LCA(one, two, nine)
    assert one is LCA(one, two, seven)
    assert one is LCA(one, one, nine)
    assert four is LCA(one, four, four)


if __name__ == '__main__':
    main()
