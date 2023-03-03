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