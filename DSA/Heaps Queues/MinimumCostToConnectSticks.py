from typing import List
from collections import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks or len(sticks) == 1:
            return 0

        minHeap = [i for i in sticks]
        heapq.heapify(minHeap)
        cost = 0

        while len(minHeap) >= 2:
            elem1, elem2 = heapq.heappop(minHeap), heapq.heappop(minHeap)
            newElem = elem1 + elem2
            cost += newElem
            heapq.heappush(minHeap, newElem)
        return cost

# TC: O(nlogn)
# SC: O(n)
