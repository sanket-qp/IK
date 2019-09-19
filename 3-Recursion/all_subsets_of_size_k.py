def all_subsets_of_size_k(nums, k):
    def subsets(nums, current_idx, k, taken, result):

        if k == 0:
            result.append(taken[:])
            return

        if current_idx == len(nums):
            # if reached here and K > 0 it means we don't have enough elements
            return

        # choice1, include current_idx
        taken.append(nums[current_idx])
        # now we have included an element K becomes K-1
        subsets(nums, current_idx + 1, k - 1, taken, result)

        # choice2, don't include current_idx
        taken.pop()
        subsets(nums, current_idx + 1, k, taken, result)

    taken = []
    result = []
    subsets(nums, 0, k, taken, result)
    return result


def main():
    pass


if __name__ == '__main__':
    n = [1, 2, 3, 4]
    k = 3
    print all_subsets_of_size_k(n, k)
