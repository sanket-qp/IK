"""
https://leetcode.com/problems/search-in-rotated-sorted-array/


Approach: Find the minimum element's index first
          Then if the target < right then we need to search in range [min, right]
          else search in range [0, min]

          In order to find minimum:
            if start > end then there are 2 possiblities
                if start > mid: that means minimum is in range [start, mid-1] e.g. [5, 1, 2, 3, 4]
                if start < mid: that means minimum is in range [mid+1, end]  e.g. [4, 5, 6, 7, 0, 1, 2]]
            else start < end
                search in [start, mid-1] e.g. [1, 2, 3, 4, 5, 6]
"""
import sys


class Solution(object):

    def get_minimum_index(self, nums, start, end):
        min_so_far = sys.maxint
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] < min_so_far:
                min_idx = mid
                min_so_far = nums[mid]

            if nums[start] > nums[end]:
                if nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                end = mid - 1
        return min_idx

    def _search(self, nums, target, start, end):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the index of the minimum element
        min_idx = self.get_minimum_index(nums, 0, len(nums) - 1)

        if nums[min_idx] == target:
            return min_idx

        # if target < right: search [min, right]
        right = len(nums) - 1
        if target <= nums[right]:
            return self._search(nums, target, min_idx + 1, right)
        else:
            # else search [0, min-1]
            return self._search(nums, target, 0, min_idx - 1)


def main():
    soln = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert 4 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [0, 1, 2, 3, 4, 5, 6]
    assert 0 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [1, 2, 3, 4, 5, 0]
    assert len(nums) - 1 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [5, 6, 7, 8, 0, 1, 2, 3, 4]
    assert 4 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [2, 3, 4, 5, 6, 0, 1]
    assert len(nums) - 2 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [5, 1, 2, 3, 4]
    assert 1 == soln.get_minimum_index(nums, 0, len(nums) - 1)

    nums = [2, 3, 4, 5, 6, 0, 1]
    target = 6
    assert 4 == soln.search(nums, target)

    nums = [2, 3, 4, 5, 6, 0, 1]
    target = 2
    assert 0 == soln.search(nums, target)

    nums = [2, 3, 4, 5, 6, 0, 1]
    target = 1
    assert len(nums) - 1 == soln.search(nums, target)

    nums = [2, 3, 4, 5, 6, 0, 1]
    target = 44
    assert -1 == soln.search(nums, target)

    nums = [0, 1, 2, 3, 4]
    target = 4
    assert len(nums) - 1 == soln.search(nums, target)

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert 4 == soln.search(nums, target)

    nums = [5, 1, 2, 3, 4]
    target = 1
    assert 1 == soln.search(nums, target)


if __name__ == '__main__':
    main()
