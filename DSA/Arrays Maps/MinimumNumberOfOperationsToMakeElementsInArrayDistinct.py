from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        steps = 0
        while len(nums) > 0:
            counter = Counter(nums)
            if (set(counter.values())) == {1}:
                return steps

            nums = nums[3:]
            steps += 1
        return steps

# TC: O((n // 3) * n) = O(n^2 // 3) = O(n^2)
# SC: O(n)
