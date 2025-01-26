from typing import List
from collections import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(minHeap, matrix[i][j])

        for _ in range(k):
            elem = heapq.heappop(minHeap)
        return elem

# TC: O(n^2 * log(n^2))
# SC: O(n^2)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0])
        minHeap = []

        for j in range(n):
            heapq.heappush(minHeap, (matrix[0][j], 0, j))

        for _ in range(k):
            val, row, col = heapq.heappop(minHeap)

            if row + 1 < n:
                heapq.heappush(minHeap, (matrix[row + 1][col], row + 1, col))

        return val
    
# TC: O(nlogn + klogn)
# SC: O(n)
