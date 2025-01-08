from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cache = {}

        def memo(left, right):
            if len(cardPoints) - k == right - left + 1:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            leftCard = cardPoints[left] + memo(left + 1, right)
            rightCard = cardPoints[right] + memo(left, right - 1)

            cache[(left, right)] = max(leftCard, rightCard)
            return cache[(left, right)]

        return memo(0, len(cardPoints) - 1)

## MLE
# TC: O(k^2)
# SC: O(k^2)


