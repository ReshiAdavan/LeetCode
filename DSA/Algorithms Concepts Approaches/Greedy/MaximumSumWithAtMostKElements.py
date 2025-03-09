import heapq
from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxHeap = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxHeap.append([-grid[i][j], i])
        heapq.heapify(maxHeap)

        maxiSum = 0
        while k:
            num, row = heapq.heappop(maxHeap)
            if limits[row]:
                maxiSum += num
                limits[row] -= 1
                k -= 1
        return -maxiSum

# TC: O((n * m) * log(n * m))
# SC: O(n * m)
