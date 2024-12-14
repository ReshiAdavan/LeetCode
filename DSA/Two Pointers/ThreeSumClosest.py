from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        miniDiff = float("inf")
        res = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            twoSumTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curSum = nums[left] + nums[right]
                diff = twoSumTarget - curSum
                if diff == 0:
                    return target

                if abs(diff) < abs(miniDiff):
                    miniDiff = diff
                    res = nums[i] + nums[left] + nums[right]

                if diff > 0:
                    left += 1
                else:
                    right -= 1
        return res

# TC: O(n^2)
# SC: O(1)
