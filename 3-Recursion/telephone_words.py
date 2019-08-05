"""
"""
keys_to_letters = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PRS',
    8: 'TUV',
    9: 'WXY'
}


def x__telephone_words(numbers, start, taken, result):
    """
    this logic is looping one time extra, investigate why
    """

    if start == len(numbers):
        result.append(taken[:])
        return

    for idx in range(start, len(numbers)):
        n = numbers[idx]
        for jdx, char in enumerate(keys_to_letters.get(n, [])):
            taken[idx] = char
            x__telephone_words(numbers, idx + 1, taken, result)
            taken[idx] = None


def __telephone_words(numbers, start, taken, result):
    if start == len(numbers):
        result.append(taken[:])
        return

    for idx in range(3):
        _char = keys_to_letters.get(numbers[start])[idx]
        taken[start] = _char
        __telephone_words(numbers, start + 1, taken, result)
        taken[start] = None


def telephone_words(numbers):
    result = []
    taken = [None] * len(numbers)
    __telephone_words(numbers, 0, taken, result)
    return result


def main():
    numbers = [8, 6, 6, 2, 6, 6, 5]
    result = telephone_words(numbers)
    print len(result)
    for x in result:
        print x


if __name__ == '__main__':
    main()
