"""
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a k-ary tree T, containing N nodes. You have to find height of the tree.
(Length of the longest path from root to any node.)

(We are looking for number of edges on longest path from root to any node,
not number of nodes on longest path from root to any node.)

Definition from Wikipedia: A k-ary tree is a rooted tree in which each node has no
more than k children. A binary tree is the special case where k=2.

solution can be found here: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):

    def __init__(self):
        self.max_depth = 0

    def maxDepthOne(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        if not root.children or len(root.children) == 0:
            return 1

        temp = []
        for c in root.children:
            temp.append(1 + self.maxDepth(c))
        return max(temp)

    def maxDepthTwo(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def _maxDepth(node, taken):
            if not node:
                return

            if not node.children:
                path = taken + [node]
                # print [x.val for x in path]
                self.max_depth = max(self.max_depth, len(path))
                return

            taken.append(node)
            for c in node.children:
                _maxDepth(c, taken)
            taken.pop()

        taken = []
        _maxDepth(root, taken)
        return self.max_depth
