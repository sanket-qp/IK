"""
https://leetcode.com/problems/factor-combinations/

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:

    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.

Examples:
    Input: 1
    Output: []

    Input: 37
    Output:[]

    Input: 12
    Output:
    [
      [2, 6],
      [2, 2, 3],
      [3, 4]
    ]

    Input: 32
    Output:
    [
    [2, 16],
    [2, 2, 8],
    [2, 2, 2, 4],
    [2, 2, 2, 2, 2],
    [2, 4, 4],
    [4, 8]
    ]

"""


class Solution(object):

    def getFactors(self, n):
        def factors(n, start, taken, result):
            if n == 1 and len(taken) > 1:
                result.append(taken[:])
                return

            for i in range(start, n + 1):
                if n % i != 0:
                    continue

                taken.append(i)
                factors(n / i, i, taken, result)
                taken.pop()

        taken = []
        result = []
        start = 2
        factors(n, start, taken, result)
        return result


def main():
    soln = Solution()
    result = soln.getFactors(32)
    for x in result:
        print x


if __name__ == '__main__':
    main()
