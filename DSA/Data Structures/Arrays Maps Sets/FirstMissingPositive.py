from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n + 1):
            flag = False
            for n in nums:
                if n == i:
                    flag = True
                    break
            if not flag:
                return i
        return n + 1

## TLE
# TC: O(n^2)
# SC: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
 
        for i in range(1, n + 1):
            if i not in nums:
                return i
        return n + 1

# TC: O(n)
# SC: O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            v = abs(nums[i])
            if v <= n:
                nums[v - 1] = -abs(nums[v - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

# TC: O(n)
# SC: O(1)
