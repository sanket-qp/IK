"""
You are given an integer array arr, of size n. Group and rearrange them (in-place) into
evens and odds in such a way that group of all even integers appears on the left side
and group of all odd integers appears on the right side.
"""
import random

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def group_the_numbers(arr, start, end):
    pivot_idx = 0
    pivot = arr[pivot_idx]
    left_ptr = 0
    right_ptr = end
    while left_ptr <= right_ptr:
        if is_even(arr[left_ptr]):
            left_ptr += 1

        if is_odd(arr[right_ptr]):
            right_ptr -= 1

        if right_ptr <= left_ptr:
            break

        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]


def main():
    N = 50
    arr = [random.randint(0, 10) for _ in range(random.randint(10, N))]
    num_of_evens = len([n for n in arr if is_even(n)])
    group_the_numbers(arr, 0, len(arr)-1)

    # after grouping, all even elements should be between 0, num_of_evens
    # and all odd elements should be between num_of_evens, len(arr)
    for i in range(num_of_evens):
        assert is_even(arr[i])

    for i in range(num_of_evens, len(arr)):
        assert is_odd(arr[i])


if __name__ == '__main__':
    main()