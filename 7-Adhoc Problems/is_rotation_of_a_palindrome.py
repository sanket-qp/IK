"""
Approach: Just try each rotation starting from each index and compare if that rotation is palindrome or not
Time Complexity: O(N*N/2) = O(N^2)
                 O(N) for trying each rotation at each index
                 O(N/2) to see if that rotation is palindrome or not

Space Complexity: O(1)
"""


def is_palindrome(s, start_idx):
    end_idx = start_idx - 1 if start_idx != 0 else len(s) - 1
    while start_idx != end_idx:
        # print "start: %s, end: %s, start_char: %s, end_char: %s" % (start_idx, end_idx, s[start_idx], s[end_idx])
        if s[start_idx] != s[end_idx]:
            return False

        start_idx = (start_idx + 1) % len(s)
        end_idx -= 1
        if end_idx < 0:
            end_idx = len(s) - 1

    return True


def is_rotation_of_a_palindrome(s):
    start_idx = 0
    while True:
        if is_palindrome(s, start_idx):
            # print "palindrome: [%s:%s]" % (start_idx, start_idx-1)
            return True, start_idx, start_idx - 1
        start_idx += 1
        start_idx = start_idx % len(s)
        if start_idx == 0:
            break

    return False, None, None


def main():
    s = "adamm"
    assert (True, 4, 3) == is_rotation_of_a_palindrome(s)

    s = "adaamma"
    assert (True, 5, 4) == is_rotation_of_a_palindrome(s)

    s = "aab"
    assert (True, 1, 0) == is_rotation_of_a_palindrome(s)

    s = "adamma"
    assert (False, None, None) == is_rotation_of_a_palindrome(s)


if __name__ == '__main__':
    main()
