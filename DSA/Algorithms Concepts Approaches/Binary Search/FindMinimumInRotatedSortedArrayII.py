from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        le, ri = 0, len(nums) - 1

        while le < ri:
            mid = (le + ri) // 2

            if nums[mid] == nums[le] == nums[ri]:
                le += 1
                ri -= 1
            elif nums[mid] <= nums[ri]:
                ri = mid
            else:
                le = mid + 1
        return nums[le]

# TC: O(log n)
# SC: O(1)
