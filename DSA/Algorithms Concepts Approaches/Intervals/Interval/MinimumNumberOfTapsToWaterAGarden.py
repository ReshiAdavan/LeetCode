from typing import List
from collections import heapq

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        tapIntervals = []
        for i, r in enumerate(ranges):
            tapIntervals.append([i - r, i + r])
        tapIntervals.sort()

        start, res, idx = 0, 0, 0
        maxHeap = []

        while start < n:
            while idx < len(ranges) and start >= tapIntervals[idx][0]:
                heapq.heappush(maxHeap, -tapIntervals[idx][1])
                idx += 1

            if not maxHeap:
                return -1
            
            start = -heapq.heappop(maxHeap)
            res += 1
        
        return res

# TC: O(qlogq)
# SC: O(q)
