"""
Given a string s of length n, find the length of the longest substring ss, that contains
exactly two distinct characters.

eceba -> ece
e -> None
baabcbab -> baab
ababababa -> ababababa


Approach: We'll use expand and reset approach. We'll keep expanding on the right until distinct characters in
          a substring so far is less than 3. Once we have 3 distinct characters we'll start shrinking the substring
          from left as long as distinct characters in the substring so far are greater than 2

          Time Complexity: O(N)
          Space Complexity: O(1)
"""


def longest_substr(s):
    start = end = 0
    chars_so_far = set()
    max_so_far = 1
    substr_so_far = None
    result = None

    while end < len(s):
        while len(chars_so_far) <= 2 and end < len(s):
            chars_so_far.add(s[end])
            end += 1

        if end == len(s):
            return s[start:end]

        substr_so_far = s[start:end - 1]
        if len(substr_so_far) > max_so_far:
            max_so_far = len(substr_so_far)
            result = substr_so_far

        while len(chars_so_far) > 2:
            chars_so_far.remove(s[start])
            start += 1

    return result


def main():
    assert "ece" == longest_substr("eceba")
    assert None is longest_substr("e")
    assert "baab" == longest_substr("baabcbab")
    assert "ababababa" == longest_substr("ababababa")


if __name__ == '__main__':
    main()
