from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum + 1) // 2
        cache = {}

        def memo(i, total):
            if total >= target or i == len(stones):
                return abs(stoneSum - 2 * total)
            if (i, total) in cache:
                return cache[(i, total)]

            A = memo(i + 1, total)
            B = memo(i + 1, total + stones[i])
            cache[(i, total)] = min(A, B)
            return cache[(i, total)]

        return memo(0, 0)

# S = sum(stones)
# TC: O(N * S)
# SC: O(N * S)
