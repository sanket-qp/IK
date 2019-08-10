import sys

"""
Implementation of Binary Search Tree
"""


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def is_leaf(self):
        return (not self.left and not self.right)

    def __str__(self):
        return "(%d, %s)" % (self.key, self.data)

    def __cmp__(self, other):

        if not other:
            return -1

        if self.key < other.key:
            return -1
        elif self.key > other.key:
            return 1
        else:
            return 0

    def __hash__(self):
        return id(self)


class Tree:
    def __init__(self):
        self.root = None
        self.element_found = False

    def xinsert(self, key, data):
        # create a node to enter
        node = Node(key, data)
        # check if root exist
        if not self.root:
            self.root = node
        else:
            # find correct place to insert the node
            current = self.root
            parent = current
            is_left_child = False
            while (current):
                parent = current
                if node.key < current.key:
                    current = current.left
                    is_left_child = True
                else:
                    current = current.right
                    is_left_child = False

            if is_left_child:
                parent.left = node
            else:
                parent.right = node

        return node

    def insert(self, key, data):
        # print "adding key : %d" % key
        node = Node(key, data)
        if not self.root:
            self.root = node
        else:
            n, parent, is_left = self.search(key)
            # print "node : %s, parent : %s" % (n, parent)
            if key <= parent.key:
                parent.left = node
            else:
                parent.right = node
        return node

    def remove(self, key):
        if not self.root:
            return None
        elif self.root.key == key:
            self.root = None
        else:
            n, parent, is_left = self.search(key)
            # if node is leaf, then just disconnect it from parent
            if not n.left and not n.right:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            elif n.right is None:
                if is_left:
                    parent.left = n.left
                else:
                    parent.right = n.left
            elif n.left is None:
                if is_left:
                    parent.left = n.right
                else:
                    parent.right = n.right
            else:
                successor = self._successor(n)
                parent.right = successor
                successor.left = n.left

    def _successor(self, node):
        current = node.right
        successor_parent = current
        successor = current
        while (current):
            successor_parent = successor
            successor = current
            current = current.left

        if successor != node.right:
            successor_parent.left = successor.right
            successor.right = node.right

        return successor

    def search(self, key):
        parent = None
        current = self.root
        is_left = False
        while (current):
            parent = current
            if key == current.key:
                return current, parent, is_left
            elif key < current.key:
                current = current.left
                is_left = True
            else:
                current = current.right
                is_left = False

        return (None, parent, is_left)

    def _height(self, root):
        if not root:
            return 0

        return 1 + max(self._height(root.left), self._height(root.right))

    def height(self):
        return self._height(self.root)

    def traverse(self):
        return self._preorder(self.root)

    def levelorder(self):
        return self._levelorder(self.root)

    def _levelorder(self, current):
        return self._levelorder_bfs(self.root)

    def _xlevelorder_bfs(self, current):
        queue = []
        stack = []
        queue.append(current)
        stack.append(1)
        childern = 0
        next_level = []
        while queue:
            current = queue.pop(0)
            sys.stdout.write("%s " % current)

            if current.left:
                next_level.append(current.left)

            if current.right:
                next_level.append(current.right)
                childern += 1

            if len(queue) == 0:
                print ""
                temp = queue
                queue = next_level
                next_level = temp

    def _levelorder_bfs(self, current):
        queue = []
        queue.append(current)
        c_nodes = 1
        next_nodes = 0
        while queue:
            current = queue.pop(0)
            sys.stdout.write("%s " % current)
            c_nodes -= 1

            if current.left:
                queue.append(current.left)
                next_nodes += 1

            if current.right:
                queue.append(current.right)
                next_nodes += 1

            if (c_nodes == 0):
                print ""
                c_nodes = next_nodes
                next_nodes = 0

    def _levelorder_dfs(self):
        for level in range(self.height()):
            self._print_level(self.root, level + 1)
            print ""

    def to_list(self):
        lists = []
        l = []
        queue = []
        current = self.root
        current_nodes = 1
        next_nodes = 0
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print "%d, %d" % (current_nodes, next_nodes)
            l.append(current)
            current_nodes -= 1

            if (current.left):
                queue.append(current.left)
                next_nodes += 1

            if (current.right):
                queue.append(current.right)
                next_nodes += 1

            if current_nodes == 0:
                lists.append(l)
                l = []
                current_nodes = next_nodes
                next_nodes = 0

        return lists

    def _print_level(self, root, level):
        if not root:
            return

        if level == 1:
            sys.stdout.write("%s " % root)
        else:
            self._print_level(root.left, level - 1)
            self._print_level(root.right, level - 1)

    def _preorder(self, current):
        if not current: return
        print "%s" % current
        self._preorder(current.left)
        self._preorder(current.right)

    def _preorder_stack(self, current):
        stack = []
        stack.append(current)
        while (stack):
            e = stack.pop()
            print e
            if e.right: stack.append(e.right)
            if e.left: stack.append(e.left)

    def _postorder(self, current):
        if not current: return
        self._postorder(current.left)
        self._postorder(current.right)
        print "%s" % current

    def _postorder_stack(self, current):
        stack = []
        stack.append(current)
        while stack:
            if current: stack.append(current)
            if current.right: stack.append(current.right)
            current = current.left

            if not current:
                print "%s" % ["%s" % x for x in stack]
                left = stack.pop()
                right = stack.pop()
                root = stack.pop()

                print "%s" % left
                print "%s" % right
                print "%s" % root

                right = stack.pop()
                current = right
                stack.append(right)

                print "%s" % ["%s" % x for x in stack]

    def _inorder(self, current):
        if not current: return
        self._inorder(current.left)
        print "%s" % current
        self._inorder(current.right)

    def _LCA(self, root, p, q):
        print "%s, %d, %d, max : %d, min : %d" % (root, p, q, max(p, q), min(p, q))
        if (not root): return None
        if (not p or not q): return None
        if root.key > max(p, q):
            return self._LCA(root.left, p, q)
        elif root.key < min(p, q):
            return self._LCA(root.right, p, q)
        else:
            return root

    def LCA(self, p, q):
        return self._LCA(self.root, p, q)

    def _vertical_sum(self, node, index, d):
        if not node:
            return

        current_sum = d.get(index, 0)
        d[index] = current_sum + node.key
        self._vertical_sum(node.left, index - 1, d)
        self._vertical_sum(node.right, index + 1, d)

    def vertical_sum(self):
        d = {}
        self._vertical_sum(self.root, 0, d)
        print d

    def _find_min(self, node):
        current = node
        parent = current
        if not current: return None
        while current:
            parent = current
            current = current.left

        return parent

    def _inorder_successor(self, node, n):
        current = node
        if not current: return None
        s = None
        while (current and current.key != n):
            if n < current.key:
                s = current
                current = current.left
            else:
                current = current.right

        # if current has right child, successor is the mininum key node of right child
        if current and current.right:
            s = self._find_min(current.right)

        return s

    def inorder_successor(self, n):
        return self._inorder_successor(self.root, n)


def main():
    t = Tree()
    t.insert(100, "Hello 100")
    t.insert(50, "Hello 50")
    t.insert(150, "Hello 150")
    t.insert(25, "Hello 25")
    t.insert(75, "Hello 75")
    t.insert(125, "Hello 125")
    t.insert(175, "Hello 175")
    t.insert(22, "Hello 22")
    t.insert(44, "Hello 44")
    t.insert(88, "Hello 88")
    t.insert(188, "Hello 188")
    t.insert(144, "Hello 144")
    t.insert(72, "Hello 144")

    print "in order"
    t._inorder(t.root)
    print "----------------------------"
    print "pre order"
    t._preorder(t.root)
    print "-----------------------------"
    print "pre order using stack"
    t._preorder_stack(t.root)

    print "======================="
    print "post order"
    t._postorder(t.root)
    print "------------------------------"

    print "height : %d" % t.height()
    t._levelorder_dfs()
    for l in t.to_list():
        print "-->".join(["%s" % x for x in l])
        print ""

    print "-----------------------"
    print "Level "
    t._print_level(t.root, t.height())
    print "%s" % t.root
    print "LCA (22, 44) : %s" % t.LCA(100, 50)
    print "inorder successor : %s" % t.inorder_successor(144)


if __name__ == "__main__":
    main()
