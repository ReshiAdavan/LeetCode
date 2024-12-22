class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <= 1:
            return False
        i = 0
        H = set()
        while i < len(nums):
            if nums[i] in H:
                return True
            H.add(nums[i])
            i += 1
        return False

# Beats 72.80% python submissions in runtime
# Beats 21.54% python submissions in memory usage  