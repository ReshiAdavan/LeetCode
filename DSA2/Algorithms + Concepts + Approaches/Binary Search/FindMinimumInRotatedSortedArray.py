class Solution(object):
    def findMin(self, nums):
        l, r, mini = 0, len(nums) - 1, nums[0]
        while l <= r:
            mid = (l + r) // 2
            mini = min(mini, nums[mid], nums[l], nums[r])
            if mini == nums[l] or mini == nums[mid]:
                r = mid - 1
            elif mini == nums[r]:
                l = mid + 1
            else:
                break
        return mini

# Beats 96.79% python submissions in runtime
# Beats 81.84% python submissions in memory usage  