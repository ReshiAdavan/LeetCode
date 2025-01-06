from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
    
# TC: O(n)
# SC: O(n)
