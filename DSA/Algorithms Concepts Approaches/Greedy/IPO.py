from typing import List
from collections import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap = [(c, i) for i, c in enumerate(capital)]
        heapq.heapify(capitalHeap)
        profitsHeap = []

        for _ in range(k):
            while capitalHeap and w >= capitalHeap[0][0]:
                i = heapq.heappop(capitalHeap)[1]
                heapq.heappush(profitsHeap, (-profits[i], i))

            if not profitsHeap:
                break

            profit = -heapq.heappop(profitsHeap)[0]
            w += profit
        return w

# Let C rep. size of capital, P rep. size of profits.
# TC: O(ClogC + max(k, C)(logC + PlogP))
# SC: O(C + P)
