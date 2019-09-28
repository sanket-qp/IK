"""
Radix tree is nothing but a compact Trie.



if subtree has more than one $, it means that that node is prefix of more than one suffixes.
so a repeating substring is a prefix which has more than one $ in it's subtree

"""

TERMINATION_CHAR = '$'


class RadixTreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []

    def is_end_of_word(self):
        return TERMINATION_CHAR in self.children

    def is_root(self):
        return self.key is None

    def __str__(self):
        root = "Root: [%s] --> " % self.key
        children = "[%s] -- ".join(child.key for child in self.children)
        return root + children


class RadixTree:
    def __init__(self):
        # node with None key is the root of the tree
        self.root = RadixTreeNode(None)

    def add_word(self, word):
        self.__add_word(self.root, word)

    def __add_word(self, node, word):
        """
        algorithm for adding a word

        Find a child which matches the first character of given word, i.e word[0]
        If we find such child, then start matching the rest of the word until it mismatches,
        Split the child node from the point of mismatch in to two nodes

        Example: if children are ['ab$', 'xy$'] and we want to add 'abc'
                 We find a child 'ab$'
                 'abc' matches until 'ab' i.e idx=2 of 'ab$'
                 we split the node in to two nodes
                        'ab'
                         |
                    '$'-----'c$'
        """
        if not word:
            raise Exception("can't add empty word")

        print "Adding word: %s" % word

        # find any child which starts with word[0]
        current = node
        child_found = False
        for child in current.children:
            # once you find the child, start matching
            if child.key.startswith(word[0]):
                print "found child: %s which starts with: %s" % (child, word[0])
                child_found = True
                split_idx = self.__split_node(child, word)
                self.__add_word(child, word[split_idx:])

        if not child_found:
            print "no child starts with: %s" % (word[0])
            # if you come here, then there isn't any child which starts with word[0]
            key = word + TERMINATION_CHAR
            print "adding a new node: %s" % key
            new_child = RadixTreeNode(key)
            current.children.append(new_child)

    def __split_node(self, node, word):
        # find the index where word mismatches with the node's key
        mismatch_idx = self.__mismatch_index(node.key, word)

        # if mismatch_idx == len(node.key) that means full key is matching and we need to
        # add the remaining word in the children
        if mismatch_idx < len(node.key):
            # split this node from mismatch_idx
            node.key = node.key[:mismatch_idx]
            print "splitting a node in to %s and %s" % (node.key, word[mismatch_idx:])
            termination_node = RadixTreeNode(TERMINATION_CHAR)
            node.children.append(termination_node)
        return mismatch_idx

    def __mismatch_index(self, node_key, word):
        print "finding mismatch between node: %s, word: %s" % (node_key, word)
        idx = 0
        while idx < len(node_key):
            if node_key[idx] != word[idx]:
                break
            idx += 1
        return idx

    @staticmethod
    def from_string(s):
        def all_suffixes(s):
            for idx in range(len(s) - 1, -1, -1):
                yield s[idx:]

        tree = RadixTree()
        for suffix in all_suffixes(s):
            print suffix
            tree.add_word(suffix)
        return tree

    def level_order(self):
        lst = []
        queue = [(self.root, 0)]
        prev_level = current_level = 0
        temp_lst = []
        while queue:
            node, current_level = queue.pop(0)
            if prev_level != current_level:
                print temp_lst
                lst.append(temp_lst[:])
                temp_lst = []

            temp_lst.append(node.key)
            for child in node.children:
                queue.append((child, current_level + 1))
            prev_level = current_level

        if temp_lst:
            print temp_lst


def main():
    s = "banana"
    # radix_tree = RadixTree.from_string(s)
    tree = RadixTree()
    tree.add_word("ab")
    print "---------"
    tree.add_word("bc")
    print "---------"
    tree.add_word("abc")
    print "---------"
    tree.add_word("bcc")
    print "---------"
    tree.add_word("bcef")
    print "---------"
    tree.add_word("abcd")
    print "---------"
    tree.add_word("xyz")

    tree.level_order()


if __name__ == '__main__':
    main()
