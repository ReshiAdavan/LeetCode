from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        numPiles = len(piles)
        cache = {}

        def dfs(pileIdx, numCoinsLeft) -> int:
            if (pileIdx, numCoinsLeft) in cache:
                return cache[(pileIdx, numCoinsLeft)]

            if pileIdx == numPiles or numCoinsLeft == 0:
                return 0

            res = dfs(pileIdx + 1, numCoinsLeft)
            
            curPileValue = 0
            for j in range(min(numCoinsLeft, len(piles[pileIdx]))):
                curPileValue += piles[pileIdx][j]
                res = max(res, curPileValue + dfs(pileIdx + 1, numCoinsLeft - j - 1))

            cache[(pileIdx, numCoinsLeft)] = res
            return cache[(pileIdx, numCoinsLeft)]

        return dfs(0, k)

# Time Complexity: O(P * k)
## P represents the total dimensions of the piles matrix
# Space Complexity: O(len(piles) * k)
# Beats 25.30% of python users in runtime
# Beats 31.67% of python users in memory usage

