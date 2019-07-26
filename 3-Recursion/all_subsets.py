
import inspect


def __all_subsets(menu, i, taken):

    print i, taken
    print "------------"

    if i == len(menu):
        # print taken
        return

    taken.append(menu[i])
    __all_subsets(menu, i+1, taken)
    taken.pop()
    __all_subsets(menu, i+1, taken)


def all_subsets(menu):
    taken = []
    __all_subsets(menu, 0, taken)


def main():
    menu = ['a', 'b', 'c']
    all_subsets(menu)

if __name__ == '__main__':
    main()