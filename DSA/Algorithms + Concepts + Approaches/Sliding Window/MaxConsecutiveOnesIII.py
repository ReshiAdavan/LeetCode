from typing import List 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maxi = 0

        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif k > 0:
                right += 1
                k -= 1
            else:
                while nums[left] == 1:
                    left += 1
                k += 1
                left += 1
            maxi = max(maxi, right - left)
        return maxi

# TC: O(n)
# SC: O(1)
