from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curSum = sum(cardPoints[0: k])
        maxScore = curSum

        left, right = k - 1, len(cardPoints) - 1
        for _ in range(k):
            curSum -= cardPoints[left]
            left -= 1

            curSum += cardPoints[right]
            right -= 1

            maxScore = max(maxScore, curSum)
        return maxScore

# TC: O(k)
# SC: O(1)
