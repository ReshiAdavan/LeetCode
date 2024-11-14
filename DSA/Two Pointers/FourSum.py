from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSumRecursive(nums, target, 4)
    
    def kSumRecursive(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []
        L = len(nums)

        # Two-sum
        if k == 2:
            left, right = 0, L - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
            return res

        # Recursive case for k-sum (k > 2)
        for i in range(L):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            # Recurse to find (k-1)-sum with updated target
            sub_results = self.kSumRecursive(nums[i + 1:], target - nums[i], k - 1)
            for sub_result in sub_results:
                res.append([nums[i]] + sub_result)
        return res

# TC: O(n^3) but generally O(n^(k-1))
# SC: O(k) for recursive stack, O(n^(k-1)) for solutions
