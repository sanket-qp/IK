"""
You are given string s of length n, having m wildcard characters '?', where each wildcard character represent
a single character.

Write a program which returns list of all possible distinct strings
that can be generated by replacing each wildcard characters in s with either '0' or '1'.

Any string in returned list must not contain '?' character i.e. you have to replace all '?'
with either '0' or '1'.


Sample Test Case 1:
Sample Input 1:
    s = "1?10"
Sample Output 1:
    result = ["1010", "1110"] or ["1110", "1010"].
Explanation 1:
    "?" at index 1 (0 based indexing) can be replaced with either '0' or '1'. So, generated
    two strings replacing "?" with '0' and '1'.

Sample Test Case 2:
Sample Input 2:
    s = "1?0?"
Sample Output 2:
    result = ["1000", "1001", "1100", "1101"] or any other list having same strings but in different order.
Explanation 2:
    Input string have two '?' characters. Each one can be replaced with either '0' or '1'.
    So, total 2*2 strings are possible as ('?' at index 1, '?' at index 3) can be replaced with
    ('0','0'), ('0','1'), ('1', '0'), ('1', '1').


Approach:
    We find the first wild card character in the string and explore two branches by placing '0' and '1' on that index and recursively calling the function on those branches
    once we are done from both the branches, we should put back the wildcard so that remaining branches can be explored

"""


def __strings_from_wildcard(s, idx, wildcard, result):
    if idx == len(s):
        result.append("".join(s))
        return

    if s[idx] != wildcard:
        __strings_from_wildcard(s, idx + 1, wildcard, result)
    else:
        s[idx] = '0'
        __strings_from_wildcard(s, idx + 1, wildcard, result)
        s[idx] = '1'
        __strings_from_wildcard(s, idx + 1, wildcard, result)
        # backtrack the wildcard after exploring both possibilities so that
        # other branches can be explored
        s[idx] = wildcard


def strings_from_wildcard(s, wildcard):
    result = []
    __strings_from_wildcard(list(s), 0, wildcard, result)
    return result


def main():
    wildcard = '?'

    s = "??"
    actual = strings_from_wildcard(s, wildcard)
    assert 4 == len(actual)
    assert ["00", "01", "10", "11"] == actual

    s = "1?0?"
    actual = strings_from_wildcard(s, wildcard)
    assert 4 == len(actual)
    assert ["1000", "1001", "1100", "1101"] == actual

    s = "1?0?1?"
    actual = strings_from_wildcard(s, wildcard)
    assert 8 == len(actual)


if __name__ == '__main__':
    main()