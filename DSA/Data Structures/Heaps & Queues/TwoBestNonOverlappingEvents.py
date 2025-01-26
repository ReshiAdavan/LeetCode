from typing import List
from collections import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        maxScore = 0
        ans = 0

        for start, end, value in events:
            while pq and pq[0][0] < start:
                maxScore = max(maxScore, heapq.heappop(pq)[1])
            ans = max(ans, maxScore + value)
            heapq.heappush(pq, (end, value))

        return ans

# TC: O(nlogn)
# SC: O(n)
