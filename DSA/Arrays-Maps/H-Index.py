from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paperCounts = [0] * (n + 1)

        # first pass
        for count in citations:
            paperCounts[min(count, n)] += 1

        # second pass
        citationCount = 0
        for i in range(n, -1, -1):
            citationCount += paperCounts[i]
            if citationCount >= i:
                return i
        return 0

# TC: O(n)
# SC: O(n)
