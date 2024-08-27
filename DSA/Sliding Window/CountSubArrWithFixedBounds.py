class Solution:
    def countSubarrays(self, nums: list[int], mink: int, maxK: int) -> int:
        res = 0
        badIdx = leftIdx = rightIdx = -1
        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                badIdx = i
            if num == mink:
                leftIdx = i
            if num == maxK:
                rightIdx = i
            res += max(0, min(leftIdx, rightIdx) - badIdx)
        return res