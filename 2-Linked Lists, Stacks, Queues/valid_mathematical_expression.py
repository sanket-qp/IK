
OPEN_PARENS = "([{"
CLOSE_PARENS = ")]}"
OPERATORS = "+-*"

def matching_open_paren(close_paren):
    return OPEN_PARENS[CLOSE_PARENS.index(close_paren)]

def is_open_paren(char):
    try:
        return OPEN_PARENS.index(char) >= 0
    except:
        return False

def is_closed_paren(char):
    try:
        return CLOSE_PARENS.index(char) >= 0
    except:
        return False

def is_digit(char):
    return char.isdigit()

def is_operator(char):
    try:
        return OPERATORS.index(char) >= 0
    except:
        return False

def calculate(digit_1, digit_2, operator):
    d1 = int(digit_1)
    d2 = int(digit_2)

    if operator == '+':
        return d1 + d2
    elif operator == '-':
        return d1 - d2
    elif operator == '*':
        return d1 * d2

def is_valid(expr):
    paren_stack = []
    digits_operator_stack = []

    for idx, char in enumerate(expr):
        if is_open_paren(char):
            paren_stack.append(char)
        elif is_closed_paren(char):
            if len(paren_stack) == 0:
                return False
            open_paren = paren_stack.pop()
            if open_paren != matching_open_paren(char):
                return False
        elif is_operator(char):
            digits_operator_stack.append(char)
        elif is_digit(char)  and len(digits_operator_stack) > 0 and is_operator(digits_operator_stack[-1]):
            operator = digits_operator_stack.pop()
            if len(digits_operator_stack) == 0:
                return False
            digit_2 = digits_operator_stack.pop()
            result = calculate(char, digit_2, operator)
            digits_operator_stack.append(result)
        else:
            digits_operator_stack.append(char)

    return len(paren_stack) == 0 and len(digits_operator_stack) <= 1


def main():
    assert True is is_open_paren('(')
    assert True is is_open_paren('[')
    assert True is is_open_paren('{')

    assert False is is_open_paren(')')
    assert False is is_open_paren(']')
    assert False is is_open_paren('}')

    assert False is is_closed_paren('(')
    assert False is is_closed_paren('[')
    assert False is is_closed_paren('{')

    assert True is is_closed_paren(')')
    assert True is is_closed_paren(']')
    assert True is is_closed_paren('}')

    assert '(' == matching_open_paren(")")
    assert '[' == matching_open_paren("]")
    assert '{' == matching_open_paren("}")

    expr = "((1+2)*3)"
    assert True is is_valid(expr)

    expr = "((1+2)*3*)"
    assert False is is_valid(expr)

    expr = ")((1+2)*3)"
    assert False is is_valid(expr)

    expr = "{[()]}"
    assert True is is_valid(expr)

    expr = "1"
    assert True is is_valid(expr)

    expr = "1+2*3"
    assert True is is_valid(expr)

if __name__ == '__main__':
    main()