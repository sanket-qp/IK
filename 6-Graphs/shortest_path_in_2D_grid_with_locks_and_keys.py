"""
https://leetcode.com/problems/shortest-path-to-get-all-keys/

We are given a 2-dimensional grid.
 "." is an empty cell,
 "#" is a wall,
 "@" is the starting point,
 '+' = Ending cell (goal),
 ("a", "b", ...) are keys, and
 ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.
We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English
alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key;
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.
"""


class CollectedKeys:
    def __init__(self, available_keys):
        # print "HERE", available_keys
        self.available_keys = available_keys
        self.collected_keys = [False] * len(available_keys)
        # print "HERE", self.collected_keys

    def add_key(self, key):

        if key not in self.available_keys:
            raise Exception("Invalid key: %s" % key)

        idx = self.available_keys.index(key)
        self.collected_keys[idx] = True

    def has_key(self, key):
        idx = self.available_keys.index(key)
        return self.collected_keys[idx]

    def has_all(self):
        for key in self.collected_keys:
            if not key:
                return False
        return True

    def __str__(self):
        rtn = []
        for idx, k in enumerate(self.collected_keys):
            if k:
                rtn.append(self.available_keys[idx])
        return "[" + " - ".join(rtn) + "]"

    def __hash__(self):
        return hash(self.__str__())


class State:
    def __init__(self, row, col, keys, num_moves):
        self.row = row
        self.col = col
        self.keys = tuple(sorted(keys))
        self.num_moves = num_moves

    def add_key(self, key):
        if key not in self.keys:
            l = list(self.keys)
            l.append(key)
            self.keys = tuple(sorted(l))

    def __str__(self):
        return "[%s: %s] [moves: %s] [keys: %s]" % (self.row, self.col, self.num_moves, self.keys)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.keys == other.keys  # and self.num_moves == other.num_moves

    def __hash__(self):
        x = "%s:%s:%s" % (self.row, self.col, self.keys)
        # x = self.__str__()
        return hash(x)


class Solution(object):

    def __init__(self):
        self.available_keys = "abcdef"
        self.locks = "ABCDEF"
        # self.keys = CollectedKeys(self.available_keys)

    def __out_of_bounds(self, grid, row, col):
        if row < 0 or row >= len(grid):
            return True

        if col < 0 or col >= len(grid[row]):
            return True

        return False

    def xneighbors(self, grid, row, col):
        n = []
        for n_row, n_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if self.__out_of_bounds(grid, n_row, n_col):
                continue

            if self.is_wall(grid, n_row, n_col):
                continue

            if self.is_lock(grid, n_row, n_col) and not self.has_key(grid[n_row][n_col]):
                continue

            n.append((n_row, n_col))

        return n

    def neighbors(self, grid, state, keys):
        n = []
        row, col = state.row, state.col
        for n_row, n_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):

            if self.__out_of_bounds(grid, n_row, n_col):
                continue

            cell = grid[n_row][n_col]

            if self.is_wall(grid, n_row, n_col):
                continue

            # if a cell is locked and we don't have the key
            if self.is_lock(grid, n_row, n_col) and cell.lower() not in state.keys:
                continue

            n.append((n_row, n_col))

        return n

    def neighbors_new(self, grid, row, col, keys):
        n = []
        for n_row, n_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if self.__out_of_bounds(grid, n_row, n_col):
                continue

            if self.is_wall(grid, n_row, n_col):
                continue

            if self.is_lock(grid, n_row, n_col) and grid[n_row][n_col].lower() not in keys:
                continue

            n.append((n_row, n_col))

        return n

    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        row_start, col_start = -1, -1
        row_end, col_end = -1, -1
        available_keys = set()
        available_locks = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if self.is_start_cell(grid, row, col):
                    row_start, col_start = row, col
                elif self.is_end_cell(grid, row, col):
                    row_end, col_end = row, col
                elif self.is_key(grid, row, col):
                    available_keys.add(grid[row][col])
                elif self.is_lock(grid, row, col):
                    available_locks.add(grid[row][col])

        self.keys = CollectedKeys("".join(available_keys))
        self.available_keys = available_keys
        # return self.__shortest_path(grid, row_start, col_start, row_end, col_end)

        visited = set()
        keys = set()
        return self.BFS(grid, row_start, col_start, keys, visited)

        # path = []
        # num_moves = 0
        # row_start, col_start = 2, 0
        # result = []
        # has_all_keys, num_moves = self.DFS(grid, row_start, col_start, visited, keys, path, result)
        # print has_all_keys, path
        #
        # for path in sorted(result):
        #     print path, len(path)

        # for row in range(len(grid)):
        #     for col in range(len(grid[row])):
        #         has_all_keys, num_moves = self.DFS(grid, row, col, visited, keys, path)
        #         if has_all_keys:
        #             print num_moves
        #             print path
        #             print "------"
        # return num_moves

    def print_queue(self, queue):
        print "Queue: %s" % ["%s" % e for e in queue]

    def print_visited(self, visited):
        print "Visited: %s" % ["%s" % e for e in visited]

    def BFS(self, grid, row_start, col_start, keys, visited):
        initial_state = State(row_start, col_start, [], 0)
        queue = [initial_state]
        total_moves = -1
        parents = {}
        parents[initial_state] = None
        final_state = None
        prev_state = None
        while queue:
            state = queue.pop(0)
            parents[state] = prev_state
            cell = grid[state.row][state.col]
            print "current state: %s, cell value: %s" % (state, cell)
            self.print_queue(queue)

            if state in visited:
                print "already visited: %s" % state
                continue

            if self.is_key(grid, state.row, state.col) and cell not in state.keys:
                keys.add(grid[state.row][state.col])
                state.add_key(cell)
            print "HELLO current state: %s, cell value: %s" % (state, cell)
            visited.add(state)

            if self._collected_all(state.keys):
                total_moves = state.num_moves
                print "FINAL STATE: %s" % state
                final_state = state
                break

            for neighbor_row, neighbor_col in self.neighbors(grid, state, keys):
                neighbor_state = State(neighbor_row, neighbor_col, state.keys, state.num_moves + 1)
                if neighbor_state not in visited:
                    print "Adding neighbor: %s" % neighbor_state
                    queue.append(neighbor_state)
            self.print_queue(queue)

            prev_state = state
            print "---------"

        if total_moves == -1:
            print "not possible"
        else:
            print "total_moves", total_moves

        rtn = []
        if final_state:
            while True:
                rtn.append(final_state)
                final_state = parents.get(final_state, None)
                if not final_state:
                    break

        for s in rtn:
            print "%s" % s
        return total_moves

    def DFS(self, grid, row, col, visited, keys, path, result):
        if self._collected_all(keys):
            print "HERE", keys, visited
            result.append(path[:])
            return True, len(path)

        if self.is_key(grid, row, col):
            keys.add(grid[row][col])

        _key = (tuple(keys), (row, col))
        visited.add(_key)

        for n_row, n_col in self.neighbors_new(grid, row, col, keys):
            _key = (tuple(keys), (n_row, n_col))
            if _key in visited:
                continue

            path.append((n_row, n_col))
            self.DFS(grid, n_row, n_col, visited, keys, path, result)
            path.pop()

        return False, len(path)

    def _collected_all(self, keys):
        for available_key in self.available_keys:
            if available_key not in keys:
                return False
        return True

    def __shortest_path(self, grid, row_start, col_start, row_end, col_end):
        queue = []
        parents = {}
        visited = set()
        num_moves = 0
        queue.append((row_start, col_start, num_moves))
        parents[(row_start, col_start)] = None

        while queue:
            row, col, num_moves = queue.pop(0)
            print grid[row][col], (row, col), num_moves

            if self.is_key(grid, row, col):
                self.keys.add_key(grid[row][col])

            print "keys: %s" % self.keys
            print "------"

            if self.keys.has_all():
                print "HERE", num_moves
                break

            # if self.is_end_cell(grid, row, col):
            #     print "found"
            #     break

            visited.add((row, col))

            for n_row, n_col in self.neighbors(grid, row, col):
                # if (n_row, n_col) in visited:
                #    continue

                parents[(n_row, n_col)] = (row, col)
                queue.append((n_row, n_col, num_moves + 1))

        if not self.keys.has_all():
            return -1

        path = []
        cell = (row, col)
        path.append(cell)
        while True:
            if not parents[cell]:
                break
            path.append(parents[cell])
            cell = parents[cell]

        print path
        return num_moves

    def has_all_keys(self, grid):
        return self.keys.has_all()

    def is_start_cell(self, grid, row, col):
        return grid[row][col] == '@'

    def is_end_cell(self, grid, row, col):
        return grid[row][col] == '+'

    def is_wall(self, grid, row, col):
        return grid[row][col] == '#'

    def is_land(self, grid, row, col):
        return grid[row][col] == '.'

    def is_key(self, grid, row, col):
        return grid[row][col] in self.available_keys

    def is_lock(self, grid, row, col):
        return grid[row][col] in self.locks

    def has_key(self, lock):
        return self.keys.has_key(lock.lower())


def main():
    grid = ["@.a.#",
            "###.#",
            "b.A.B",
            "...+"]
    soln = Solution()
    # assert 8 == soln.shortestPathAllKeys(grid)

    grid = ["@", "A", "a"]
    # assert -1 == soln.shortestPathAllKeys(grid)

    grid = ["@...a",
            ".###A",
            "b.BCc"]
    # print "Total Moves: %s" % soln.shortestPathAllKeys(grid)

    grid = ["..#....##.",
            "....d.#.D#",
            "#...#.c...",
            "..##.#..a.",
            "...#....##",
            "#....b....",
            ".#..#.....",
            "..........",
            ".#..##..A.",
            ".B..C.#..@"]
    print "Total Moves: %s" % soln.shortestPathAllKeys(grid)

    # keys = CollectedKeys("abcdef")
    # keys.add_key("a")
    # keys.add_key("f")
    # print "%s" % keys
    # print keys.__hash__()
    # keys.add_key("f")
    # print keys.__hash__()
    # keys.add_key("f")
    # print keys.__hash__()
    #
    # print keys.has_key("d")


if __name__ == '__main__':
    main()
