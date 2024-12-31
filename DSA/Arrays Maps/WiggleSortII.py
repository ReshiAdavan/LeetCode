from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sNums = sorted(nums)
        mid = (n + 1) // 2

        j, k = mid - 1, n - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sNums[j]
                j -= 1
            else:
                nums[i] = sNums[k]
                k -= 1
        return nums

# TC: O(nlog(n))
# SC: O(n)

