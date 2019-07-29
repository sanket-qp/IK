"""
A palindromic decomposition of string is a decomposition of the string into substrings,
such that all those substrings are valid palindromes.

Given a string s, you have to find ALL possible palindromic decompositions of it.
Note that string s itself is also a substring of s.


Approach: split the string in each possible ways and recurse on remaining string
For example, split the string "madam" in to splits of
                               m, adam -> recurse on (adam) keep the first split it is palindrome
                               ma, dam -> recurse on (dam)
                                          we won't explore this recursion as 'ma' is not palindrome and we want all the splits a palindrome
                               mad, am -> recurse on (am)
                               mada, m -> recurse on (m)

"""


def is_pali(s):
    return s == s[::-1]


def __all_palindromic_decompositions(s, stack, result):
    if len(s) == 0:
        result.append('|'.join(stack))
        return

    # try substring of each length, and recurse on remaining string
    for idx in range(len(s)):
        first_split = s[:idx + 1]
        # we want all the decomposed substrings to be palindrome
        # if first split is not palindrome then there is no point
        # in testing the rest of the split
        if is_pali(first_split):
            stack.append(first_split)
            # recurse on remaining split
            second_split = s[idx + 1:]
            __all_palindromic_decompositions(second_split, stack, result)
            # backtrack to previous level so we can explore remaining states
            stack.pop()


def all_palindromic_decompositions(s):
    result = []
    stack = []
    __all_palindromic_decompositions(s, stack, result)
    return result


def main():
    s = "madam"
    assert ['m|a|d|a|m', 'm|ada|m', 'madam'] == all_palindromic_decompositions(s)
    print "---------------"

    s = "aaa"
    assert ['a|a|a', 'a|aa', 'aa|a', 'aaa'] == all_palindromic_decompositions(s)

    s = "abcd"
    assert ['a|b|c|d'] == all_palindromic_decompositions(s)

    s = "abracadabra"
    assert ['a|b|r|a|c|a|d|a|b|r|a', 'a|b|r|a|c|ada|b|r|a',  'a|b|r|aca|d|a|b|r|a'] == all_palindromic_decompositions(s)


if __name__ == '__main__':
    main()
