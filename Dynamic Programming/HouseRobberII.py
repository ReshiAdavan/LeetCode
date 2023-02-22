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