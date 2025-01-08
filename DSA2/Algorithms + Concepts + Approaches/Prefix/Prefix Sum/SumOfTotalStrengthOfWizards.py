from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        total = 0

        for i in range(n):
            for j in range(i, n):
                currGroup = strength[i: j + 1]
                mini = min(currGroup)
                curSum = sum(currGroup)
                total = (total + mini * curSum) % MOD
        return total

## TLE
# TC: O(n^3)
# SC: O(n)

from itertools import accumulate

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        # previous smaller elements
        prevSmaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        # next smaller elements
        nextSmaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                nextSmaller[i] = stack[-1]
            stack.append(i)

        # prefix sum of prefix sum of strength
        prefixSum = list(accumulate(strength, initial=0))
        prePrefixSum = list(accumulate(prefixSum, initial=0))

        total = 0
        for i in range(n):
            # boundaries where strength[i] is min
            left = prevSmaller[i] + 1
            right = nextSmaller[i] - 1

            leftCount = i - left + 1
            rightCount = right - i + 1

            # sums using prefix of prefix sums

            # Negative contribution: subarrays to the left
            neg_sum = (prePrefixSum[i + 1] - prePrefixSum[i - leftCount + 1]) % MOD

            # Positive contribution: subarrays to the right
            pos_sum = (prePrefixSum[i + rightCount + 1] - prePrefixSum[i + 1]) % MOD

            contribution = strength[i] * (pos_sum * leftCount - neg_sum * rightCount)
            total = (total + contribution) % MOD

        return total % MOD

# TC: O(n)
# SC: O(n)
