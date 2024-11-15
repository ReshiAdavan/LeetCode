class Solution(object):
    def minEatingSpeed(self, piles, h):
        if len(piles) == h:
            return max(piles)
        l, r, k = 1, max(piles), 0
        while l <= r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += ((p - 1) // m) + 1
            if t <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k 

# Beats 97.23% python submissions in runtime
# Beats 79.61% python submissions in memory usage

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        left = 1
        right = max(piles)
        k = 0

        while left <= right:
            middle = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil((pile / middle))
            if time <= h:
                k = middle
                right = middle - 1
            else:
                left = middle + 1
        return k
    
# TC: O(nlog(max(piles)))
# SC: O(1)
