from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxPrev = values[0] + 0
        maxScore = 0

        for j in range(1, len(values)):
            score = maxPrev + values[j] - j
            maxScore = max(maxScore, score)
            maxPrev = max(maxPrev, values[j] + j)
        return maxScore

# TC: O(n)
# SC: O(1)
