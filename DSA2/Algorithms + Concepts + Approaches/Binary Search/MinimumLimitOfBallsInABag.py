from typing import List
from math import ceil

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivideWithPenalty(penalty: int) -> bool:
            operations = 0
            for balls in nums:
                operations += ceil(balls / penalty) - 1
                if operations > maxOperations:
                    return False
            return True

        low, high = 1, max(nums)
        limit = high

        while low <= high:
            mid = (low + high) // 2

            if canDivideWithPenalty(mid):
                limit = mid
                high = mid - 1
            else:
                low = mid + 1

        return limit

# TC: O(nlogn)
# SC: O(1)
