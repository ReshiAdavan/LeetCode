class Solution(object):
    def twoSum(self, nums, target):
        N = {}
        for x, y in enumerate(nums):
            diff = target - y
            if diff in N:
                return [N[diff], x]
            N[y] = x

# Beats 97.86% python submissions in runtime
# Beats 86.61% python submissions in memory usage  