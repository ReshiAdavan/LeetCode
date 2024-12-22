from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        cache = {}

        def memo(i, o1, o2):
            if i >= len(nums):
                return 0
            if (i, o1, o2) in cache:
                return cache[(i, o1, o2)]

            # no operations
            A = nums[i] + memo(i + 1, o1, o2)
            B = C = D = E = float("inf")

            # perform op1
            if o1:
                B = (nums[i] + 1) // 2 + memo(i + 1, o1 - 1, o2)
            # perform op2
            if o2 and nums[i] >= k:
                C = (nums[i] - k) + memo(i + 1, o1, o2 - 1)
            # perform op1 then op2
            if o1 and o2 and (nums[i] + 1) // 2 >= k: 
                D = (nums[i] + 1) // 2 - k + memo(i + 1, o1 - 1, o2 - 1)
            # perform op2 then op1
            if o1 and o2 and nums[i] >= k:
                E = (nums[i] - k + 1) // 2 + memo(i + 1, o1 - 1, o2 - 1)
            cache[(i, o1, o2)] = min(A, B, C, D, E)
            return cache[(i, o1, o2)]
        return memo(0, op1, op2)

# TC: O(N * op1 * op2)
# SC: O(N * op1 * op2)
