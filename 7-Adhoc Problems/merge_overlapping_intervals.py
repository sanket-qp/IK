"""
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def overlaps(current_interval, merged_interval):
    i1_start, i1_end = current_interval[0], current_interval[1]
    i2_start, i2_end = merged_interval[0], merged_interval[1]

    if i2_start <= i1_start <= i2_end:
        return True

    if i1_start <= i2_start <= i1_end:
        return True

    if i2_start <= i1_end <= i2_end:
        return True

    if i1_start <= i2_end <= i1_end:
        return True

    return False


def merge(current_interval, merged_interval):
    i1_start, i1_end = current_interval[0], current_interval[1]
    i2_start, i2_end = merged_interval[0], merged_interval[1]
    return (min(i1_start, i2_start), max(i1_end, i2_end))


def merged_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort()

    merged_interval = intervals[0]
    result = []
    for idx in range(1, len(intervals)):
        current_interval = intervals[idx]
        if overlaps(current_interval, merged_interval):
            merged_interval = merge(current_interval, merged_interval)
        else:
            result.append(merged_interval)
            merged_interval = current_interval

    result.append(merged_interval)
    return result


def main():
    assert True is overlaps((-100, 100), (1, 10))
    assert False is overlaps((-100, 0), (1, 10))
    assert True is overlaps((-100, 0), (0, 100))
    assert True is overlaps((2, 4), (1, 5))
    assert True is overlaps((1, 5), (2, 4))

    assert (1, 4) == merge((1, 2), (2, 4))

    intervals = [(1, 3), (5, 7), (2, 4), (6, 8)]
    assert [(1, 4), (5, 8)] == merged_intervals(intervals)

    intervals = [(100, 154), (13, 47), (1, 5), (2, 9), (7, 11), (51, 51), (47, 50)]
    assert [(1, 11), (13, 50), (51, 51), (100, 154)] == merged_intervals(intervals)

    intervals = [(1, 100), (-100, 0)]
    assert [(-100, 0), (1, 100)] == merged_intervals(intervals)

    intervals = [(1, 10), (2, 20), (3, 30), (4, 40)]
    assert [(1, 40)] == merged_intervals(intervals)


if __name__ == '__main__':
    main()
