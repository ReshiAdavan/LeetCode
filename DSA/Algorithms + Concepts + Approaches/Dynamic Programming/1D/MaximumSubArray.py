# Kadane’s Algorithm - DP
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

class Solution(object):
    def maxSubArray(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        localMax = 0
        globalMax = float('-inf')

        x = 0
        while x < length:
            localMax = max(nums[x], nums[x] + localMax)
            globalMax = max(localMax, globalMax)
            x += 1
        return globalMax

# Beats 91.71% python submissions in runtime
# Beats 72.13% python submissions in memory usage

from typing import List

## Recursive Memoization
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}

        def memo(start):
            if start >= len(nums):
                return 0

            if start in cache:
                return cache[start]

            # include
            A = nums[start] + memo(start + 1)

            # exclude and start fresh
            B = nums[start]

            cache[start] = max(A, B)
            return cache[start]

        maxi = float('-inf')
        for i in range(len(nums)):
            maxi = max(maxi, memo(i))
        return maxi

# TC: O(N)
# SC: O(N)

 