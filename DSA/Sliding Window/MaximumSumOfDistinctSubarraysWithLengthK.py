from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        maxi = 0
        window = set()
        curSum = 0

        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                curSum -= nums[left]
                left += 1


            window.add(nums[right])
            curSum += nums[right]

            if right - left == k - 1:
                maxi = max(maxi, curSum)
                curSum -= nums[left]
                window.remove(nums[left])
                left += 1

        return maxi
    
# TC: O(n)
# SC: O(k)
