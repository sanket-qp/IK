"""
Trie is a data structure which is useful in prefix (i.e substring) searches in linear time.

Every substring of a string is a prefix of a suffix. so if we want to deal with substring problems
then we can build trie of all suffixes. and prefix (i.e. substring) search in this trie will be easy.

Time Complexity: There are N^2 suffixes, so it takes O(N^2) to build a suffix trie.
                 O(M) to search for the substring (i.e prefix)
                 O(N^2) + O(M) same as brute force.

                But there is another data structure, called, Suffix Trees that can be built in O(N)
                using Ukkonen's algorith, which is quite complex and time consuming.
                So in interview setting, solve the problem using Trie and just mention the O(N) suffix trees.

                so linear time substring search can be achieved by suffix trees.


suffix trie/tree can help solve following problems:
    most repeating substring
    longest repeating substring

"""
from trie import Trie


def all_suffixes(s):
    for idx in range(len(s) - 1, -1, -1):
        yield s[idx:]


def build_suffix_trie(s):
    trie = Trie()
    for suffix in all_suffixes(s):
        trie.add_word(suffix)
    return trie


def search(s, substr):
    trie = build_suffix_trie(s)
    # substr is a prefix
    return len(trie.match_prefix(substr)) != 0


def all_substrings(s):
    for length in range(1, len(s) + 1):
        idx = 0
        while idx + length < (len(s) + 1):
            yield s[idx: idx + length]
            idx += 1


def main():
    s = "mississippi"
    s = "abcd"
    for substr in all_substrings(s):
        print "hello", substr
        assert True is search(s, substr)
    assert False is search(s, "isxsi")


if __name__ == '__main__':
    main()
