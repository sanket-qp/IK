"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://www.youtube.com/watch?v=qpgqhp_9d1s
"""


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, reminder = divmod(sum(nums), k)
        if reminder:
            return False

        used = [False] * len(nums)
        return self.__can_be_partitioned(nums, 0, used, k, 0, target)

    def __can_be_partitioned(self, nums, start_idx, used, k, in_progress_group_sum, target):
        if k == 1:
            return True

        if in_progress_group_sum > target:
            return False

        if in_progress_group_sum == target:
            return self.__can_be_partitioned(nums, 0, used, k - 1, 0, target)

        for idx in range(start_idx, len(nums)):
            if not used[idx] and in_progress_group_sum + nums[idx] <= target:
                used[idx] = True
                if self.__can_be_partitioned(nums, idx + 1, used, k, in_progress_group_sum + nums[idx], target):
                    return True
                used[idx] = False

        return False


def main():
    soln = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    assert True is soln.canPartitionKSubsets(nums, k)

    nums = [4, 1, 1, 1, 1, 1, 1]
    k = 3
    assert False is soln.canPartitionKSubsets(nums, k)

    nums = [5, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3]
    k = 15
    assert True is soln.canPartitionKSubsets(nums, k)

    nums = [2, 2, 2, 2, 3, 4, 5]
    k = 4
    assert False is soln.canPartitionKSubsets(nums, k)

    nums = [780, 935, 2439, 444, 513, 1603, 504, 2162, 432, 110, 1856, 575, 172, 367, 288, 316]
    k = 4
    assert True is soln.canPartitionKSubsets(nums, k)

    nums = [815, 625, 3889, 4471, 60, 494, 944, 1118, 4623, 497, 771, 679, 1240, 202, 601, 883]
    k = 3
    assert True is soln.canPartitionKSubsets(nums, k)


if __name__ == '__main__':
    main()
