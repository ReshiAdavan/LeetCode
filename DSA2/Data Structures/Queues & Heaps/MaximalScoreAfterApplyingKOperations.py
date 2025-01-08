from typing import List
from collections import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = [-num for num in nums]
        heapq.heapify(heap)

        while k > 0:
            elem = heapq.heappop(heap)
            elem *= -1
            score += elem
            elem = ceil(elem / 3)
            heapq.heappush(heap, -elem)
            k -= 1
        return score

# Time Complexity: O(klog(n))
# Space Complexity: O(n)
