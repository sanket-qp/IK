"""
You are given n balls. Each of these balls are of one the three colors: Red, Green and
Blue. They are arranged randomly in a line. Your task is to rearrange them such that all
balls of the same color are together and their collective color groups are in this order:
Red balls first, Green balls next and Blue balls last.

This combination of colors is similar to the Dutch National Flag, hence the problem name.

Approach 1: Partition the array such that All BLUE balls are at end and all Green & Red are in the beginning.
            Now Partition the beginning part of the array so that All GREEN balls are at the end

            Time Complexity: O(n) + O(n) = O(n)
            Space Complexity: no additional space needed


Approach 2:
            Maintain 4 Regions
            [0 -> current] = RED
            [current -> mid] = GREEN
            [mid -> last] = BLUE
            We start with
            [current -> last] = UNKNOWN

            Whenever we encounter a RED ball, we swap it with left most GREEN
            Whenever we encouter GREEN ball, we just continue
            Whenever we encounter BLUE ball, we swap it with the last ball

            We maintain two indices i.e left_most_green_ball and last_ball, and iterate through the array from start to end

            Time Complexity: O(n)
            Space Complexity: no additional space needed

"""

import random

RED = 0
GREEN = 1
BLUE = 2

def partition_by_green(arr, start, end):
    pivot_idx = start
    pivot = arr[start]
    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1

        while end >= end and arr[end] > pivot:
            end -= 1

        if end > start:
            arr[start], arr[end] = arr[end], arr[start]

    partition_idx = end
    arr[pivot_idx], arr[partition_idx] = arr[partition_idx], arr[pivot_idx]
    return partition_idx

def swap_red_and_green(arr, start, end):
    while start <= end:
        while arr[start] == RED:
            start += 1

        while arr[end] == GREEN:
            end -= 1

        if end > start:
            arr[start], arr[end] = arr[end], arr[start]

def move_ball_to_first(arr, COLOR):
    for idx, ball in enumerate(arr):
        if ball == COLOR :
            arr[0], arr[idx] = arr[idx], arr[0]
            break

def rearrange(arr):
    # find first Green ball and move it to the first element
    move_ball_to_first(arr, GREEN)
    print "before pattition: %s" % arr
    # first partition the array by GREEN so that GREEN OR RED <= GREEN < BLUE
    partition_idx = partition_by_green(arr, 0, len(arr)-1)
    print "partition_idx : %d" % partition_idx
    print "after partition: %s" % arr

    # then partition the first half array in to RED < GREEN
    move_ball_to_first(arr[0:partition_idx+1], RED)
    print "after moving: %s" % arr[0:partition_idx+1]
    # partition_idx = partition_by_green(arr[0:partition_idx+1], 0, partition_idx-1)
    # swap_red_and_green(arr, 0, partition_idx)
    partition_by_green(arr, 0, partition_idx)
    print "partition_idx : %d" % partition_idx
    print "after partition: %s" % arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dutch_flag_sort(arr):

    # maintain 4 regions
    # 0 -> low - R
    # low -> mid - G
    # mid -> high - unknown
    # high -> end - B

    left_most_green = 0
    last_char = len(arr) - 1
    current_idx = 0

    while current_idx <= last_char:
        if arr[current_idx] == RED:
            swap(arr, current_idx, left_most_green)
            current_idx += 1
            left_most_green += 1
        elif arr[current_idx] == GREEN:
            current_idx += 1
        else:
            swap(arr, current_idx, last_char)
            last_char -= 1

def main():
    N = 33
    arr = [random.randint(RED, BLUE) for _ in range(N)]
    print arr
    rearrange(arr)

    arr = [random.randint(RED, BLUE) for _ in range(N)]
    temp = sorted(arr)
    print "BEFORE sorting: %s" % arr
    dutch_flag_sort(arr)
    print "AFTER sorting: %s" % arr
    assert temp == arr

if __name__ == '__main__':

    main()