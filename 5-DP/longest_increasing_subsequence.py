"""
Find the longest increasing sub sequence from given array
LIS([2, 5, 3, 4, 1, 6]) = 4 (2, 3, 4, 6)


Recurrence relationship:
    LIS(i) = max sub sequence length ending at i
           = 1 if i == 0
           = max (LIS(j) + 1 for j in [0, i) iff arr[i] > arr[j])

    We don't need to find LIS at last index but we need to find LIS at any index, so we need to
    find the maximum from the dp array

Direction:
    Higher i depends on lower i, so we have to build the table from 0 -> end

"""
import random


def LIS_DP(arr):
    dp_table = [1] * len(arr)
    for i in range(0, len(arr)):
        if i == 0:
            dp_table[i] = 1
        else:
            temp = []
            for j in range(0, i):
                if arr[i] > arr[j]:
                    temp.append(dp_table[j] + 1)
                else:
                    temp.append(1)
            dp_table[i] = max(temp)

    ## print "dp", dp_table

    # now find the actual sequence
    # We'll start from the max_idx and go down to 0
    # We'll subtract 1 from max_value and try to find it in dp_array
    # We can only add the value in dp_array if and only if it added to the increasing sequence

    longest_seq_len = 0
    max_idx = -1
    for idx, _len in enumerate(dp_table):
        if _len >= longest_seq_len:
            longest_seq_len = _len
            max_idx = idx

    longest_seq = []
    longest_seq.append(arr[max_idx])
    dp_idx = max_idx
    while dp_idx > 0:
        seq_len = dp_table[dp_idx]
        j = dp_idx - 1
        done = True
        while j >= 0:
            if dp_table[j] == seq_len - 1 and arr[dp_idx] > arr[j]:
                longest_seq.insert(0, arr[j])
                dp_idx = j
                done = False
                break
            j -= 1

        if done:
            break
    return longest_seq


def main():
    arr = [2, 3, 5, 4, 1, 6, 1, 2, 8]
    longest_seq = LIS_DP(arr)
    assert 5 == len(longest_seq)
    assert [2, 3, 4, 6, 8] == longest_seq

    arr = [5, 4, 3, 2, 1]
    longest_seq = LIS_DP(arr)
    assert 1 == len(longest_seq)
    assert [1] == longest_seq

    N = 8
    arr = [random.randint(1, 100) for _ in range(N)]
    # arr = [57, 23, 73, 89, 96, 51, 13, 39]
    print arr
    longest_seq = LIS_DP(arr)
    print longest_seq


if __name__ == '__main__':
    main()
