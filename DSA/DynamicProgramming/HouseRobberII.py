class Solution(object):
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        r1, r2 = 0, 0

        for n in nums:
            newRob = max(r1 + n, r2)
            r1 = r2
            r2 = newRob
        return r2

# Beats 98.70% python submissions in runtime
# Beats 88.63% python submissions in memory usage

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums: list[int]) -> int:
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
            i += 1
        return dp[-1]
    
# Beats 80.64% python submissions in runtime
# Beats 80.07% python submissions in memory usage