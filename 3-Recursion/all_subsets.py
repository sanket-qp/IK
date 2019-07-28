"""
Given a set (in form of string s containing only distinct lowercase letters ('a' - 'z')),
you have to generate ALL possible subsets of it .
Note that: empty set is always a subset of any set. whole set s should also be considered as its subset here.


Approach: We have two choices at each element,
            choice1, pick the element and explore rest of the string by recursing on the remaining string
            choice2, don't pick the element and explore the rest of the string by recursing on it

"""


def __all_subsets(s, current_idx, stack, result):
    if current_idx == len(s):
        result.append("".join(stack))
        return

    # choice1, add the current element in the subset and recurse on the remaining string with current element in the set
    stack.append(s[current_idx])
    __all_subsets(s, current_idx+1, stack, result)
    stack.pop()

    # choice2, explore the remaining string without adding current element to the set
    __all_subsets(s, current_idx+1, stack, result)


def all_subsets(s):
    result = []
    stack = []
    __all_subsets(s, 0, stack, result)
    return result


def main():
    s = "ab"
    assert ['', 'a', 'ab', 'b'] == sorted(all_subsets(s))

    s = "xyz"
    assert ['', 'x', 'xy', 'xyz','xz', 'y', 'yz', 'z'] == sorted(all_subsets(s))


if __name__ == '__main__':
    main()