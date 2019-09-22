"""
You are given a matrix where each number represents altitude of that cell, such that, water flows towards lower altitudes.

If a cell's four neighboring cells all have higher altitudes, we call this cell a sink. water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. If a cell is not a sink,
you may assume it has a unique lowest neighbor and that this will be lower than the cell.

Cells that drain into the same sink directly or indirectly are said to be part of the
same basin.

Your challenge is to partition the map into basins. Your code should
output the sizes of the basins, in non-decreasing order.
"""
from collections import Counter
from collections import defaultdict


def out_of_bounds(graph, row, col):
    if row < 0 or row >= len(graph):
        return True

    if col < 0 or col >= len(graph[row]):
        return True

    return False


def neighbors(graph, row, col):
    _min = graph[row][col]
    nbor = None
    for n_row, n_col in ((row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)):
        if out_of_bounds(graph, n_row, n_col):
            continue

        if graph[n_row][n_col] < _min:
            _min = graph[n_row][n_col]
            nbor = (n_row, n_col)

    if nbor:
        return [nbor]
    else:
        return []


def DFS(graph, row, col, visited, path):
    cell = (row, col)
    if cell in visited:
        return

    path.append(cell)
    visited.add(cell)
    for n_row, n_col in neighbors(graph, row, col):
        DFS(graph, n_row, n_col, visited, path)


def count_basins(graph):
    paths_ending_at = defaultdict(set)
    counter = Counter()
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            visited = set()
            path = []
            DFS(graph, row, col, visited, path)
            end_cell = path[-1] if path else None

            print "(%s,%s), path: %s" % (row, col, path)
            if end_cell:
                counter[end_cell] += 1
                paths_ending_at[end_cell].add(tuple(sorted(path[:-1])))

    for cell in counter:
        print cell, counter[cell]


def main():
    graph = [
        [1, 5, 2],
        [2, 4, 7],
        [3, 6, 9]
    ]

    assert [] == neighbors(graph, 0, 0)
    assert [(0, 0)] == neighbors(graph, 0, 1)
    # count_basins(graph)
    print "---------------"

    graph = [
        [0, 2, 1, 3],
        [2, 1, 0, 4],
        [3, 3, 3, 3],
        [5, 5, 2, 1],
    ]
    count_basins(graph)
    print "---------------"

    graph = [
        [0, 1, 2, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 2, 1, 0],
    ]
    count_basins(graph)
    print "---------------"


if __name__ == '__main__':
    main()
