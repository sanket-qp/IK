"""
Given a point p, and other n points in two-dimensional space, find k points out of n
points which are nearest to p.
NOTE: Distance between two points is measured by the standard Euclidean method.

Approach 1:
    we'll keep a max heap of K elements, every time we find an element which is less than the top element
    we'll replace top element with current/min element

    Time Complexity: O(n * log K)
    Space Complexity: O(K)


Approach 2:
    Create a list of array having distances of all points from original point,
    Then keep partitioning this array until Pivot == K
    when Pivot is moved to Kth index,
        then all elements < K are between 0 to K -1 indices
        and all elements > K are between K+1 to len(array) indices

    this algorightm is known as quick select (https://www.geeksforgeeks.org/quickselect-algorithm/)

    Time Complexity: O(n) for computing the distance + (n + n/2 + n/4 + .... + 1 = 2 * n) for partitioning the array = O(n) + O(2n) = O(n)
    Space Complexity: O(n) for storing distances array + O(K) for results = O(n+K)
"""

import random
import math
import heapq

def distance(p1, p2, inverse = False):
    x_squared = pow((p1[0] - p2[0]), 2)
    y_squared = pow((p1[1] - p2[1]), 2)
    dist = math.sqrt(x_squared + y_squared)
    return -1 * dist if inverse else dist

def nearest_neighbors(point, n_points, K):
    heap = []
    for neighbor in n_points:
        current_dist = distance(point, neighbor, True)

        if len(heap) == 0:
            heapq.heappush(heap, (current_dist, neighbor))
            continue

        closest_dist, closest_point, = heapq.nsmallest(1, heap)[0]
        if current_dist > closest_dist and len(heap) > 0:
            heapq.heappop(heap)
            heapq.heappush(heap, (current_dist, neighbor))
        elif len(heap) < K:
            heapq.heappush(heap, (current_dist, neighbor))

    result = []
    while len(heap) > 0:
        dist, point = heapq.heappop(heap)
        result.append(point)

    return result

def partition(arr, start, end):
    pivot_idx = start
    pivot = arr[pivot_idx]
    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1

        while end >= start and arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    partition_idx = end
    arr[pivot_idx], arr[partition_idx] = arr[partition_idx], arr[pivot_idx]
    return partition_idx

def top_K(arr, start, end, K):
    while (start < end):
        pivot_idx = partition(arr, start, end)
        if pivot_idx == K:
            return
        elif pivot_idx < K:
            start = pivot_idx + 1
        else:
            end = pivot_idx - 1

def nearest_neighbors_optimal(point, n_points, K):
    distances = []
    for neighbor in n_points:
        dist = distance(point, neighbor)
        distances.append((dist, neighbor))

    # shuffle the distances array
    random.shuffle(distances)
    top_K(distances, 0, len(distances)-1, K)
    result = []
    for i in range(K):
        result.append(distances[i][1])

    return result

def main():
    p = (10, 10)
    K = 3
    n = [(1, 1), (0, 1), (1, 0), (4, 4)]
    n = [(10, 10), (1, 1), (2, 2), (20, 20), (19, 19), (9,9), (8, 8)]

    assert [(8, 8), (9, 9), (10, 10)] == sorted(nearest_neighbors(p, n, K))
    assert [(8, 8), (9, 9), (10, 10)] == sorted(nearest_neighbors_optimal(p, n, K))


if __name__ == '__main__':
    main()