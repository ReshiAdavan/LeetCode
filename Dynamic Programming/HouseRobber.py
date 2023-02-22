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