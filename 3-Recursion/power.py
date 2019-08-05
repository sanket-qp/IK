"""
The problem statement is straight forward. Given a base 'a' and an exponent 'b'. Your task is to find a^b.
The value could be large enough. So, calculate a^b % 1000000007.


Approach:
keep dividing the exponent by two pow(2, 8) will be handled as follows
                                2x2x2x2 x 2x2x2x2
                                4x4 x 4x4
                                16 x 16

Time Complexity: O(b) where b is exponent
Space complexity: O(b) used by call stack
"""

count = 0


def power(a, b):
    global count
    count += 1
    if b == 1:
        return a

    ans = power(a, b / 2) * pow(a, b / 2)
    return ans * 1 if b % 2 == 0 else ans * a


def main():
    global count
    count = 1
    a = 2
    b = 4
    assert pow(a, b) == power(a, b)
    print count

    a = 3
    b = 8
    count = 1
    assert pow(a, b) == power(a, b)
    print count

    a = 2
    b = 5
    assert pow(a, b) == power(a, b)

    a = 3
    b = 9
    assert pow(a, b) == power(a, b)

    count = 1
    a = 2
    b = 33
    assert pow(a, b) == power(a, b)
    print count


if __name__ == '__main__':
    main()
