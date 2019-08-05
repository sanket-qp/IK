"""
Given a positive integer n, find ALL well formed round brackets string of length 2*n.

Example:
    n = 3
    output = ((()))
             (()())
             (())()
             ()(())
             ()()()
"""

OPEN_PAREN = '('
CLOSE_PAREN = ')'
EMPTY_SPACE = None


def is_valid(combination):
    stack = []
    for char in combination:
        if char == OPEN_PAREN:
            stack.append(char)
        elif not stack:
            return False
        else:
            stack.pop()

    return False if stack else True


def fill_empty_with_close_parens(taken):
    filled = taken[:]
    for idx, e in enumerate(filled):
        if e is EMPTY_SPACE:
            filled[idx] = CLOSE_PAREN
    return filled


def __well_formed_brackets(N, start, num_of_open_parens, taken, result):
    if start == len(taken) and num_of_open_parens != N:
        return

    if num_of_open_parens == N or start == len(taken):
        filled = fill_empty_with_close_parens(taken)
        if is_valid(filled):
            result.append("".join(filled))
        return

    for idx in range(start, len(taken)):
        taken[idx] = OPEN_PAREN
        __well_formed_brackets(N, start + 1, num_of_open_parens + 1, taken, result)
        taken[idx] = EMPTY_SPACE


def well_formed_brackets(N):
    result = []
    taken = [None] * 2 * N
    num_of_open_parens = 0
    __well_formed_brackets(N, 0, num_of_open_parens, taken, result)
    return result


def main():
    N = 3
    result = well_formed_brackets(N)
    print len(result)
    print result


if __name__ == '__main__':
    main()
