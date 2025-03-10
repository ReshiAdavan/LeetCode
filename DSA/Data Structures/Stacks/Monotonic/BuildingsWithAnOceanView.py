from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxHeightSeen = heights[-1]
        res.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxHeightSeen:
                res.append(i)
                maxHeightSeen = heights[i]

        res.sort()
        return res

# TC: O(n + nlogn)
# SC: O(1) auxillary space
