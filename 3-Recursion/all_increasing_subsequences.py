"""

"""

def combine(digit, l2):
    result = []
    result.append([digit])
    for seq in l2:
        result.append(seq)
        if seq[0] > digit:
            result.append([digit] + seq)
    return result

def __all_increasing_subsequences(seq):
    if len(seq) == 1:
        return [seq[:]]

    current_digit = seq[0]
    remaining_seqs = __all_increasing_subsequences(seq[1:])
    return combine(current_digit, remaining_seqs)


def all_increasing_subsequences(seq):
    return __all_increasing_subsequences(seq)


def __all_increasing_subseqs_with_stack(seq, current_index, taken, result):

    if current_index == len(seq):
        if len(taken) == 0:
            return
        result.append(taken[:])
        return

    current_element = seq[current_index]

    # exploring without adding current element
    __all_increasing_subseqs_with_stack(seq, current_index+1, taken, result)

    if len(taken) == 0 or taken[-1] < current_element:
        taken.append(current_element)
        __all_increasing_subseqs_with_stack(seq, current_index+1, taken, result)
        taken.pop()

def all_increasing_subseqs_with_stack(seq):
    result = []
    taken = []
    __all_increasing_subseqs_with_stack(seq, 0, taken, result)
    return result


def main():
    seq = [1, 2, 5, 8, 2, 1, 22, 4, 44]
    #seq = [5, 1, 6, 2, 44]
    all_increasing =  all_increasing_subsequences(seq)
    all_increasing_with_stack = all_increasing_subseqs_with_stack(seq)

    assert  sorted(all_increasing) == sorted(all_increasing_with_stack)


if __name__ == '__main__':
    main()