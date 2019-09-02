"""

Given a String "abadba" and a set {b, d}
    find the smallest substring which contains all the characters from the set

Approach 1: Brute Force: try all substrings from length 1 to n and see if anyone matches
            Time Complexity: O(N^2 * M)
            O(N^2 )substrings and each substring takes O(M) times to see if all characters exist in the set

Apprach 2: Expand and Reset
           Expand to the right side until the substrig is not controlling the set
           As soon as the substring controls the set start shrinking from left side
           until it stops controlling the set

           Time Complexity O(N^2) because controls_the_set is linear

Approach 3: Same as 2 but we are getting rid of controls_the_set method
            In this approach we maintain a hashmap of character frequencies

            We start with an empty hashmap, and as we traverse the string, we keep adding characters from the string
            to frequency map. When the keys in the map equals keys in the set, we know that we are controlling the set.
            i.e our substring contains all the characters from the set.

            Once we start controlling the set, we start shrinking the substring from left and start decrementing
            the frequency. When any key reaches the frequency = 0, we remove it from the map.
            And when map has less number of keys than the et, it means, we stopped controlling the set


            For example, if the string is abbda and set is (b, d)

            # Expand until we start controlling the set
            start 0, end 0: a is not in set, so continue by end += 1
                map is empty so we are not controlling the set
            start 0, end 1: b is in set so frequency map = {b:1}
                keys(map) < chars(set) so we expand by end += 1
            start 0, end 2: b is in set, so frequency map = {b:2}
                keys(map) < chars(set) so we expand by end += 1
            start 0, end 3: d is in set, so frequency map = {b:2, d:1}
                keys(map) == chars(set) so the substring [0, 3] are controlling the set. and we should shrink form left


            # Shrink until we stop controlling the set
            start 0, end 3: a is not in set, so we continue by start += 1
            start 1, end 3: b is in set, we decrement the count, so frequency map = {b:1, d:1}
                keys(map) == chars(set) so are still controlling the set, we need to continue
                start += 1
            start 2, end 3: b is in set, we decrement the count,
                here b's count reached to 0 so we should remove it from the map, so frequency map = {d:1}
                keys(map) < chars(set) so stopped controlling the set

            At this point maintain the smallest substring and keep continue expanding and shrinking

            Time Complexity: O(N)
"""

from collections import Counter


def controls_the_set(S, start, end, _set):
    """
    checks if the given substring from start:end+1 contains all the characters from the set
    """
    temp_set = _set.copy()
    for char in S[start:end + 1]:
        if char in temp_set:
            temp_set.remove(char)

        if len(temp_set) == 0:
            return True

    return False


def smallest_substring(S, _set):
    start = 0
    end = 0
    min_substr_len = len(S)
    min_substr = None

    while start < len(S) and end < len(S):
        # Expand until we start controlling
        if not controls_the_set(S, start, end, _set):
            end += 1
        else:
            # Shrink from the begining until we stop controlling the set
            while controls_the_set(S, start, end, _set):
                start += 1

            temp = S[start - 1:end + 1]
            if len(temp) < min_substr_len:
                min_substr_len = len(temp)
                min_substr = temp

    return min_substr


def smallest_substring_linear(S, _set):
    """
    We'll keep a hashmap of frequencies of the character
    when hashmap contains the character equals to length of the set, that means we are controlling the set

    When one of the keys in hashmap reaches 0, that means we stopped controlling the set
    """
    frequency = Counter()
    min_len = len(S)
    min_substr = None
    start = end = 0
    while end < len(S):
        # Expand until we start controlling
        # also maintain the frequency
        while len(frequency) != len(_set):
            if S[end] in _set:
                frequency[S[end]] += 1
            end += 1

            if end == len(S):
                break

        if end == len(S):
            break

        # Shrink from the left
        while start < len(S) and len(frequency) == len(_set):
            if S[start] in _set:
                frequency[S[start]] -= 1

                if frequency[S[start]] == 0:
                    # we just stopped controlling
                    frequency.pop(S[start])

            start += 1

        # keep track of smallest substring
        temp = S[start - 1:end]
        if len(temp) < min_len:
            min_len = len(temp)
            min_substr = temp

    return min_substr


def main():
    S = "abbdba"
    _set = set(['b', 'd'])
    # assert True is controls_the_set(S, 0, len(S), _set)
    # assert True is controls_the_set(S, 1, len(S), _set)
    # assert True is controls_the_set(S, 2, len(S), _set)
    # assert True is controls_the_set(S, 3, len(S), _set)
    # assert False is controls_the_set(S, 4, len(S), _set)

    x = smallest_substring(S, _set)
    y = smallest_substring_linear(S, _set)
    assert x == y

    S = "abbdba"
    _set = set(['b', 'd', 'c'])
    x = smallest_substring(S, _set)
    y = smallest_substring_linear(S, _set)
    assert x is None
    assert x == y

    S = "abcdba"
    _set = set(['b', 'd'])
    x = smallest_substring(S, _set)
    y = smallest_substring_linear(S, _set)
    assert 'db' == x
    assert x == y

    S = "abcdab"
    _set = set(['b', 'd'])
    x = smallest_substring(S, _set)
    y = smallest_substring_linear(S, _set)
    assert 'bcd' == x
    assert x == y


if __name__ == '__main__':
    main()
