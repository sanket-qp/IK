"""
Longest repeating substring

Approaches:

(1) Brute force: Generate all substrings and count their occurrence
             Time Complexity: O(N^4) = O(N^2) for generating all substrings
                                     + O(N^2) for num_occurrence (string compare also takes O(N))

             Space Complexity: O(1)

(2) Using radix tree:
            We'll add all the suffixes of a given string in to a radix tree.
            Then we'll find the node with most termination character ($) in it's subtree.

            A node in the radix tree represents a prefix and all the children represents suffixes
            whose prefix is a current node.

            That means that the node which has most termination characters is a prefix of more than one suffixes
            We need to find such node which has most $ under it.

            so, to find most repeating substring, we'll just find a node with maximum $ in it'subtree.

            --------

            Now, to find Longest repeating substring, we'll find a node which is farthest (i.e. longest) from the root and has
            multiple $s in it's subtree

            Example:
                banana:
                ana is a prefix of anana and ana
                ana is the Longest repeating substring

                mississippi:
                issi is prefix of issippi and issiissippi
                issi is the Longest  repeating substring

"""

from radix_tree import RadixTree


def all_substrings(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]


def num_occurrence(s, substr):
    n = 0
    for idx in range(len(s) - len(substr) + 1):
        temp = s[idx:idx + len(substr)]
        # print temp
        if temp == substr:
            n += 1
    return n


def longest_repeating_substring_brute_force(s):
    max_len = 1
    longest_so_far = s[0]
    most_occurred = 1
    for substr in all_substrings(s):
        n = num_occurrence(s, substr)
        if len(substr) > max_len and n >= most_occurred and n > 1:
            max_len = max(max_len, len(substr))
            most_occurred = n
            longest_so_far = substr
    return longest_so_far


def all_suffixes(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i:]


def xnode_with_max_termination_chars(root):
    def get_node(node):
        if not node:
            return (None, 0, 0)

        if node.is_leaf():
            return (node, 1, 1)

        _max = 0
        chosen_node = None
        _sum = 0
        for child in node.children:
            n, num, sum_child = get_node(child)
            _sum += num
            if sum_child > _max:
                _max = sum_child
                chosen_node = child
                print "chosen: %s, sum: %s" % (chosen_node, sum_child)

        print "child: %s, total: %s" % (child, _sum)
        return chosen_node, _max, _sum

    node, _max, _sum = get_node(root)
    print "node: %s, max: %s, sum: %s" % (node, _max, _sum)


def node_with_max_termination_chars(root):
    def get_max(node):
        if not node:
            return 0

        if node.is_leaf():
            return 1

        _sum = 0
        for child in node.children:
            _sum += get_max(child)
        return _sum

    max_repeating_node = None
    max_occurrence = 0
    for child in root.children:
        temp = get_max(child)
        if temp > max_occurrence:
            max_repeating_node = child
            max_occurrence = temp

    return max_repeating_node, max_occurrence


def most_repeating_substring_using_radix_tree(s):
    tree = RadixTree()
    for suffix in all_suffixes(s):
        tree.add_word(suffix)

    tree.level_order()
    return node_with_max_termination_chars(tree.root)


def longest_node_with_max_termination_chars(root):
    def get_longest(node):
        if not node:
            return 0, None

        if node.is_leaf():
            return 1, node.key

        total = 0
        longest_so_far = ""
        max_dollars = 0
        for child in node.children:
            num_dollars, longest = get_longest(child)
            total += num_dollars
            # find the longest and most repeating
            if num_dollars > max_dollars:
                longest_so_far = longest
                max_dollars = num_dollars

        longest_so_far = node.key + longest_so_far
        return total, longest_so_far

    _max = 0
    longest_repeating = None
    for child in root.children:
        total, longest = get_longest(child)
        print "%s: %s, total: %s" % (child.key, longest, total)
        if total > _max:
            _max = total
            longest_repeating = longest

    return longest_repeating[:-1]


def longest_repeating_substring_using_radix_tree(s):
    """
    root asks each of the children that give me the number of $ in your subtree and which one is the longest
    """
    tree = RadixTree()
    for suffix in all_suffixes(s):
        tree.add_word(suffix)

    longest = longest_node_with_max_termination_chars(tree.root)
    # print "longest: %s" % longest
    return longest


def main():
    assert 2 == num_occurrence("banana", "ana")
    assert 3 == num_occurrence("banana", "a")
    assert 2 == num_occurrence("banana", "na")
    assert 2 == num_occurrence("banana", "an")
    assert 1 == num_occurrence("banana", "b")
    assert 0 == num_occurrence("banana", "xyz")

    assert "ana" == longest_repeating_substring_brute_force("banana")
    assert "a" == longest_repeating_substring_brute_force("abcdef")

    node, total = most_repeating_substring_using_radix_tree("banana")
    assert "a" == node.key
    assert 3 == total

    node, total = most_repeating_substring_using_radix_tree("mississippi")
    assert "i" == node.key
    assert 4 == total

    assert "ana" == longest_repeating_substring_using_radix_tree("banana")
    assert "issi" == longest_repeating_substring_using_radix_tree("mississippi")
    assert "aaa" == longest_repeating_substring_using_radix_tree("aaaa")


if __name__ == '__main__':
    main()
