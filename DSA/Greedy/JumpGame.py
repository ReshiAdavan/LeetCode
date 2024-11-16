from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalPost:
                goalPost = i
        return True if not goalPost else False

# TC: O(n)
# SC: O(1)