from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            if x1 == x2:
                return float("inf")
            return (y2 - y1) / (x2 - x1)

        maxi = 1
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                m = slope(points[i], points[j])
                slopes[m] = slopes.get(m, 1) + 1
                maxi = max(maxi, slopes[m])
        return maxi
    
# TC: O(n^2)
# SC: O(n)
