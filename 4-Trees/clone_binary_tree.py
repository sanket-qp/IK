import random

from bst import Node
from bst import Tree as BST


def clone(root):
    def __clone(node):
        if not node:
            return

        new_root = Node(node.key, node.data)
        new_left = __clone(node.left)
        new_right = __clone(node.right)
        new_root.left = new_left
        new_root.right = new_right
        return new_root

    new_root = __clone(root)
    return new_root


def main():
    tree = BST()
    N = 10
    _set = set([random.randint(1, N * N) for _ in range(N)])
    for x in _set:
        tree.insert(x, "")

    new_root = clone(tree.root)
    new_tree = BST()
    new_tree.root = new_root

    for orig_node, cloned_node in zip(tree.levelorder_nodes(), new_tree.levelorder_nodes()):
        assert orig_node is not cloned_node
        assert orig_node.key == cloned_node.key
        assert orig_node.data == cloned_node.data


if __name__ == '__main__':
    main()
