from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i + 1, len(nums)):
                total += nums[j]
                if (j - i + 1) >= 2 and total % k == 0:
                    return True
        return False

## TLE
# TC: O(N^2)
# SC: O(1)

# Congruence (mod k)
# prefixSum[i] % k == prefixSum[j] % k => prefixSum[j] - prefixSum[i] % k => prefixSum[i:j] % k == 0

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]

            if k != 0:
                remainder = curSum % k
            else:
                remainder = curSum

            if remainder in remainders:
                if i - remainders[remainder] > 1:
                    return True
            else:
                remainders[remainder] = i

        return False

# TC: O(N)
# SC: O(N)
