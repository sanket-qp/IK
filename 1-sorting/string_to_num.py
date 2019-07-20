"""
abc 12e42 -> 12
axy++-07f -> -7
123xy456 -> 123
"""

def is_digit(char):
    return 48 <= ord(char) <= 57

def is_sign(char):
    return char == '-' or char == '+'

def char_to_digit(char):
    return ord(char) - ord('0')

def digits_to_num(lst_of_nums, is_negative = False):
    multiplier = 10
    num = 0
    for i in range(len(lst_of_nums)):
        num += pow(multiplier, i) * lst_of_nums[i]
    return -1 * num if is_negative else num

def str_to_num(_str):
    stack = []
    digit_started = False
    sign_started = False
    is_negative = False
    sign_started = False
    for char in _str:
        if is_sign(char):
            if not sign_started:
                sign_started = True
            elif digit_started:
                # if encounter a sign again in the middle of the number then just break
                break
            is_negative = True if char == '-' else False
        elif is_digit(char):
            if not digit_started:
                digit_started = True
            stack.insert(0, char_to_digit(char))
        elif digit_started:
            break
    return digits_to_num(stack, is_negative)

def main():
    _str = "12345"
    num = str_to_num(_str)
    assert num == 12345
    print "str_to_num(%s) = %d" % (_str, num)

    _str = "abc 12e4"
    num = str_to_num(_str)
    assert num == 12
    print "str_to_num(%s) = %d" % (_str, num)

    _str = "abc 444e4"
    num = str_to_num(_str)
    assert num == 444
    print "str_to_num(%s) = %d" % (_str, num)

    _str = "123xy456"
    num = str_to_num(_str)
    assert num == 123
    print "str_to_num(%s) = %d" % (_str, num)

    _str = "axy++-04f"
    num = str_to_num(_str)
    assert num == -4
    print "str_to_num(%s) = %d" % (_str, num)

    _str = "axy+4-4f"
    num = str_to_num(_str)
    assert num == 4
    print "str_to_num(%s) = %d" % (_str, num)
    
if __name__ == "__main__":
    main()
