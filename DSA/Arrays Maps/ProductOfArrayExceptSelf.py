class Solution(object):
    def productExceptSelf(self, nums):
        result, pre, post = [1] * (len(nums)), 1, 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        return result   

# Beats 61.74% python submissions in runtime
# Beats 57.27% python submissions in memory usage  