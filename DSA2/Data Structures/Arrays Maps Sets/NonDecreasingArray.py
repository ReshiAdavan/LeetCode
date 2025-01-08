class Solution(object):
    def checkPossibility(self, nums):
        error = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if error or (i > 1 and i < len(nums) - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                error = 1
        return True

# Beats 90.56% python submissions in runtime
# Beats 81.67% python submissions in memory usage