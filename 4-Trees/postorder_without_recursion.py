from bst import Tree as BST


def process(node):
    print "%s" % node


def postorder(root):
    if not root:
        return

    if root.is_leaf():
        process(root)
        return

    stack = []
    stack.append(root)
    while stack:
        top = stack[-1]
        if top.is_leaf():
            stack.pop()
            process(top)
        else:
            if top.right:
                stack.append(top.right)
                top.right = None

            if top.left:
                stack.append(top.left)
                top.left = None


def main():
    tree = BST()
    lst = [50, 25, 75, 12, 35, 55, 80]
    for _ in lst:
        tree.insert(_, "hello")

    postorder(tree.root)


if __name__ == '__main__':
    main()
