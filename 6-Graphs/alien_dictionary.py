"""
https://leetcode.com/problems/alien-dictionary/

Given a sorted dictionary of an alien language, you have to find the order of
characters in that language.

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

1. You may assume all letters are in lowercase.
2. You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
3. If the order is invalid, return an empty string.
4. There may be multiple valid order of letters, return any one of them is fine.


Example:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

----

Input:
[
  "z",
  "x"
]

Output: "zx"

----


Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return ""
"""
from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = defaultdict(set)
        for word in words:
            for char in word:
                graph[char] = set()

        for idx in range(len(words) - 1):
            word1, word2 = words[idx], words[idx + 1]
            self.addToGraph(graph, word1, word2)
        return self.topoSort(graph)

    def addToGraph(self, graph, word1, word2):
        """
        letters of word1 must appear before word2
        """
        word1_len = len(word1)
        word2_len = len(word2)
        i = 0
        while i < min(word1_len, word2_len):
            char1 = word1[i]
            char2 = word2[i]
            if char1 != char2:
                graph[char1].add(char2)
                return
            i += 1

    def topoSort(self, graph):

        ## self.printGraph(graph)
        result = []

        self.NOT_VISITED = 0
        self.VISITED = 1
        self.IN_PROGRESS = 2
        states = defaultdict(lambda: self.NOT_VISITED)

        for node in graph:
            states[node] = self.NOT_VISITED

        for node in graph.keys():
            try:
                self.DFS(node, graph, states, result)
            except Exception, e:
                return ""

        return "".join(result)

    def DFS(self, node, graph, states, result):
        if states[node] == self.VISITED:
            return

        if states[node] == self.IN_PROGRESS:
            raise Exception("Loop detected")

        states[node] = self.IN_PROGRESS

        for neighbor in graph[node]:
            self.DFS(neighbor, graph, states, result)

        states[node] = self.VISITED
        result.insert(0, node)

    def printGraph(self, graph):
        for key in graph:
            print "%s -> %s" % (key, graph[key])
        print "-------------------"


def main():
    soln = Solution()
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    assert "wertf" == soln.alienOrder(words)
    words = ["z", "x", "z"]
    assert "" == soln.alienOrder(words)
    words = ["z", "z"]
    assert "z" == soln.alienOrder(words)
    words = ["ab", "adc"]
    assert "bdca" == soln.alienOrder(words)
    words = ["ri", "xz", "qxf", "jhsguaw", "dztqrbwbm", "dhdqfb", "jdv", "fcgfsilnb", "ooby"]
    assert "" == soln.alienOrder(words)


if __name__ == '__main__':
    main()
