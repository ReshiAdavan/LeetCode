class Solution(object):
    def rob(self, nums):
        l = len(nums)
        if l == 1: return nums[0]
        if l == 2: return max(nums[0], nums[1])
        maxi = 0
        for i in range(2, l):
            for j in range(i - 1): 
                maxi = max(maxi, nums[j])
            nums[i] += maxi
        return max(nums[-1], nums[-2])

# Beats 77.06% python submissions in runtime
# Beats 89.21% python submissions in memory usage

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
            i += 1
        return dp[-1]

# Beats 99.50% python submissions in runtime
# Beats 44.35% python submissions in memory usage
