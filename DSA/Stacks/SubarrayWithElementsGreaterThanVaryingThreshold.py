from typing import List

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        stack = []

        # Fill the left boundaries
        for i in range(n):
            num = nums[i]
            while stack and nums[stack[-1]] >= num:
                left[i] = left[stack.pop()]
            stack.append(i)

        # Fill the right boundaries
        for i in range(n-1, -1, -1):
            num = nums[i]
            while stack and nums[stack[-1]] >= num:
                right[i] = right[stack.pop()]
            stack.append(i)

        for i in range(n):
            k = right[i] - left[i] + 1
            if nums[i] > threshold / k:
                return k
        
        return -1
    
# Time Complexity: O(P + N)
# Space Complexity: O(P + N)
# Beats 38.92% of python users in runtime
# Beats 18.64% of python users in memory usage
