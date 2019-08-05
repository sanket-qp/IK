"""
Write a function that will return the number of binary search trees that can be constructed with N nodes.

There may be other iterative solutions, but for the purpose of this exercise, please use recursive solution.

"""


def x__num_of_trees(N, start, remaining, taken, result):
    if start > N:
        print taken
        return

    for _ in range(start, N + 1):
        n = remaining.pop()
        last, branch = taken[-1] if taken else (None, None)
        if not taken:
            taken.append((n, 'root'))
        elif n > last:
            taken.append((n, 'right'))
        else:
            taken.append((n, 'left'))

        # remaining.remove(n)
        __num_of_trees(N, start + 1, remaining, taken, result)
        taken.pop()
        remaining.insert(0, n)


def get_remaining_right(N, n, taken):
    remaining = []
    already_used = [t[0] for t in taken]
    for x in range(n + 1, N + 1):
        if x not in already_used:
            remaining.append(x)
    # print "right of: %d, taken: %s = %s" % (n, already_used, remaining)
    return remaining


def get_remaining_left(N, n, taken):
    remaining = []
    already_used = [t[0] for t in taken]
    for x in range(1, n):
        if x not in already_used:
            remaining.append(x)
    # print "left of: %d, taken: %s = %s" % (n, already_used, remaining)
    return remaining


def valid_tree(taken):
    for n, parent, branch in taken:
        if branch == 'left' and n > parent:
            return False

        if branch == 'right' and n < parent:
            return False

    return True


def __num_of_trees(N, parent, start, remaining, taken, direction, result):
    if start > N:
        if valid_tree(taken):
            print taken
            result.append(taken[:])
        return

    if len(remaining) == 0:
        return

    # for n in range(start, N+1):
    for n in remaining:

        if not direction:
            direction = 'root'

        taken.append((n, parent, direction))
        right = get_remaining_right(N, n, taken)
        __num_of_trees(N, n, start + 1, right, taken, 'right', result)

        left = get_remaining_left(N, n, taken)
        if left:
            __num_of_trees(N, n, start + 1, left, taken, 'left', result)

        taken.pop()


def num_of_trees(N):
    remaining = range(1, N + 1)
    taken = []
    result = []
    __num_of_trees(N, None, 1, remaining, taken, None, result)
    return result


def main():
    N = 3
    result = num_of_trees(N)
    print len(result)
    print result


if __name__ == '__main__':
    main()
