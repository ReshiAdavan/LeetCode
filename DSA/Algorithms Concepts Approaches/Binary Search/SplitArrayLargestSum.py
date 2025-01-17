from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lower, upper = max(nums), sum(nums)
        res = upper

        def validator(mid):
            res = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > mid:
                    res += 1
                    curSum = n
            return (res + 1 <= k)

        while lower <= upper:
            mid = (lower + upper) // 2
            if validator(mid):
                res = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return res

# TC: O(N * log(sum(nums) - max(nums))) ~ O(N * log(sum(nums)))
# SC: O(1)
