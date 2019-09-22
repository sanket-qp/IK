"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        heights_stack = [heights[0]]
        pos_stack = [0]
        last_height = heights[0]
        last_pos = 0
        max_area = 0
        temp_area = 0
        for idx in range(1, len(heights)):
            current_h = heights[idx]
            if current_h >= heights_stack[-1]:
                heights_stack.append(current_h)
                pos_stack.append(idx)
            else:
                while heights_stack and current_h < heights_stack[-1]:
                    last_height = heights_stack.pop()
                    last_pos = pos_stack.pop()
                    temp_area = last_height * (idx - last_pos)
                    max_area = max(max_area, temp_area)

                heights_stack.append(current_h)
                pos_stack.append(last_pos)

        if heights_stack:
            final_pos = len(heights)
            while heights_stack:
                last_height = heights_stack.pop()
                last_pos = pos_stack.pop()
                temp_area = last_height * (final_pos - last_pos)
                max_area = max(max_area, temp_area)

        return max_area


def main():
    soln = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    assert 10 == soln.largestRectangleArea(heights)

    heights = [2, 3, 4, 5, 4, 3, 1]
    assert 15 == soln.largestRectangleArea(heights)

    heights = [5, 4, 3, 2, 2, 1]
    assert 10 == soln.largestRectangleArea(heights)

    heights = [1, 2, 3, 4, 2]
    assert 8 == soln.largestRectangleArea(heights)

    heights = [4, 2, 0, 3, 2, 5]
    assert 6 == soln.largestRectangleArea(heights)

    heights = [1, 2, 2]
    assert 4 == soln.largestRectangleArea(heights)


if __name__ == '__main__':
    main()
