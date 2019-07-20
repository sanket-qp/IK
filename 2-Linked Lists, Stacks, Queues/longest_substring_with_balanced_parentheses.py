"""
Given a string brackets, containing only '(' and ')', you have to find the length of the
longest substring that has balanced parentheses.
You need to find length only, not the substring itself.
()()() => 6
(( ((()) (((() => 4
"""

OPEN_PAREN = '('
CLOSE_PAREN = ')'

def longest_substring_with_balance_parens(s):
    max_len = 0
    current_len = 0
    stack = []
    new_seq = True
    for idx, char in enumerate(s):

        # if open paren and stack is not empty then it means we encountered a new sequence
        if char == OPEN_PAREN and stack:
            new_seq = True
        elif new_seq:
            # when we encounter a first close paren, then substring length starts from 0
            # and mark that we are in the middle of a new sequence by setting new_seq to False
            new_seq = False
            current_len = 0

        if char == OPEN_PAREN:
            stack.append(char)
        else:
            if stack and stack[-1] == OPEN_PAREN:
                stack.pop()
                current_len += 2
                max_len = max(max_len, current_len)
            else:
                new_seq = True
    return max_len


def main():
    assert 4 == longest_substring_with_balance_parens("((((())(((()")
    assert 6 == longest_substring_with_balance_parens("()()()")
    assert 4 == longest_substring_with_balance_parens(")()()(")
    assert 0 == longest_substring_with_balance_parens(")))(((")
    assert 6 == longest_substring_with_balance_parens(")()()()(")
    assert 2 == longest_substring_with_balance_parens(")()))()(")
    assert 0 == longest_substring_with_balance_parens("))))))))")
    assert 0 == longest_substring_with_balance_parens("((((((((")

if __name__ == '__main__':
    main()