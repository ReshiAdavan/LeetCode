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