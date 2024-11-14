from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        table = {}
        L = len(nums)
        res = []

        for i in range(L):
            target = -nums[i]
            table = {}
            for j in range(i + 1, L):
                newTarget = target - nums[j]
                if newTarget in table:
                    if sorted([nums[i], nums[j], newTarget]) not in res:
                        res.append(sorted([nums[i], nums[j], newTarget]))
                table[nums[j]] = j
        return res

# TC: O(n*n*log(n)) -> fails LC
# SC: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        L = len(nums)

        for i in range(L):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, L - 1

            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif twoSum < target:
                    left += 1
                else:
                    right -= 1
        return res

# TC: O(n*n + nlog(n)) ==> O(n*n)
# SC: O(1)
