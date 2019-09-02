"""
Implentation of trie

Problems solved: Prefix search, Pattern search

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def __str__(self):
        return " -- ".join(self.children.keys())


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.DOT = '.'

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def find_word(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False

        return current.end_of_word

    def match_prefix(self, prefix):
        current = self.root
        result = []
        for idx, char in enumerate(prefix):
            if char not in current.children:
                return []

            current = current.children[char]

        # found the node where the given prefix ends
        ## print "%s" % current.children
        taken = list(prefix)
        return self._collect_all_words(current, taken)

    def match_pattern(self, pattern):
        result = []
        path = []
        self.__match_pattern_recursive(self.root, pattern, 0, path, result)
        return result

    def __match_pattern_recursive(self, node, pattern, pattern_idx, path, result):
        if pattern_idx == len(pattern):
            if node.end_of_word:
                result.append("".join(path))
            return

        if pattern[pattern_idx] == self.DOT:
            # recursively call all children
            for char, child in node.children.items():
                path.append(char)
                self.__match_pattern_recursive(child, pattern, pattern_idx + 1, path, result)
                path.pop()
        elif pattern[pattern_idx] in node.children:
            char = pattern[pattern_idx]
            child = node.children[char]
            path.append(char)
            self.__match_pattern_recursive(child, pattern, pattern_idx + 1, path, result)
            path.pop()
        else:
            return

    def _collect_all_words(self, node, taken):
        # do a DFS from this node
        result = []
        self.DFS(node, taken, result)
        return result

    def DFS(self, node, taken, result):

        if node.end_of_word:
            result.append("".join(taken))

        if not node.children:
            return

        for char, child in node.children.items():
            taken.append(char)
            self.DFS(child, taken, result)
            taken.pop()


def main():
    trie = Trie()
    trie.add_word("hello")
    assert True is trie.find_word("hello")
    assert False is trie.find_word("he")
    trie.add_word("he")
    trie.add_word("helium")
    assert True is trie.find_word("he")

    print trie.match_prefix("he")

    words = ['CAT', 'BAT', 'CAN', 'CUT']
    trie = Trie()
    for word in words:
        trie.add_word(word)

    pattern = 'C..'
    assert ['CAT', 'CAN', 'CUT'] == trie.match_pattern(pattern)


if __name__ == '__main__':
    main()
