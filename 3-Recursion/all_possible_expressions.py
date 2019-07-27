"""
You are given a string s of length n, containing only numerical characters ('0' - '9').
You are also given a non-negative number target.

You have to put between each pair of numerical characters, one of ("", "*", "+")
operators such that the expression you get will evaluate to the target value.

You have to return ALL possible strings(expressions) that evaluate to target value.

Putting "" (an empty string) operator between two numerical characters means, that
the they are joined (e.g. 1""2 = 12).
Also the join can be extended further (e.g. 1""2""3 = 123).

Precedence of the operators matters. In higher to lower precedence:
Join ("") > Multiplication ("*") > Addition ("+")
"""


def __all_possible_expressions(s, target, stack, result):

    # base case, 1 character string
    if len(s) == 1:
        stack.append(s)
        expression = ''.join(stack)
        if eval(expression) == target:
            result.add(expression)
        stack.pop()

    for idx in range(1, len(s)+1):
        for op in ('', '*', '+'):
            first_char = s[:idx]
            remaining_str = s[idx:]
            stack.append(first_char)
            stack.append(op)
            __all_possible_expressions(remaining_str, target, stack, result)
            stack.pop()
            stack.pop()


def all_possible_expressions(s, target):
    result = set()
    stack = []
    __all_possible_expressions(s, target, stack, result)
    return list(result)


def main():
    assert ['123'] == all_possible_expressions("123", 123)
    assert ['2+22', '22+2'] == all_possible_expressions("222", 24)
    assert [] == all_possible_expressions("222", 2)


if __name__ == '__main__':
    main()