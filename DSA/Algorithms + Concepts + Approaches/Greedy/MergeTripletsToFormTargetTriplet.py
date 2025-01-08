from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxX, maxY, maxZ = float("-inf"), float("-inf"), float("-inf")

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue

            maxX = max(maxX, x)
            maxY = max(maxY, y)
            maxZ = max(maxZ, z)

        return maxX == target[0] and maxY == target[1] and maxZ == target[2]
    
# TC: O(n)
# SC: O(1)
