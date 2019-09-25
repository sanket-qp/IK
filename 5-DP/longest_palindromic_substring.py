"""
Approach:

            Recurrence relationship:
            LPS(i, j) = longest palindromic substring [i:j]
                = 2 + LPS(i+1, j-1) iff s[i] == s[j]
                = max (LPS(i, j-1), LPS(i+1, j) iff s[i] != s[j]

           s[1:5] is palindrome if s[1] == s[5] and s[2:4] is palindrome
           so we need to look for the cells (i+1, j-1) to see if the enclosing substring is palindrome
           we have to build the dp_table such that cell in the next row and previous column is already filled

           (1, 5) depends on (2, 4)
           (2, 4) depends on (3, 3)
           (3, 3) depends on (4, 2)
           (4, 2) depends on (5, 1)

           we have to build the dp_table diagonally from top-left to bottom-right
"""


def longest_palindromic_substring(s):
    dp_table = [[False] * len(s) for _ in range(len(s))]
    # initialize substrings of length 1
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                dp_table[i][j] = True

    # initialize for the substrings of length 2
    max_len = 1
    max_range = (0, 0)
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            dp_table[i - 1][i] = True
            max_len = 2
            max_range = (i - 1, i)

    # for substrings of length > 2
    for substr_len in range(3, len(s) + 1):
        for i in range(0, len(s) - substr_len + 1):
            j = i + substr_len - 1
            if s[i] == s[j] and dp_table[i + 1][j - 1]:
                dp_table[i][j] = True
                if substr_len > max_len:
                    max_len = substr_len
                    max_range = (i, j)

    start = max_range[0]
    end = max_range[1] + 1
    return s[start:end]


def main():
    s = "amadamz"
    assert "madam" == longest_palindromic_substring(s)

    s = "hello"
    assert "ll" == longest_palindromic_substring(s)

    s = "abcd"
    assert "a" == longest_palindromic_substring(s)


if __name__ == '__main__':
    main()
