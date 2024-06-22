class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2) 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

# Beats 94.39% python submissions in runtime
# Beats 53.26% python submissions in memory usage 