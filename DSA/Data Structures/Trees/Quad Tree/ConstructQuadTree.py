# Definition for a QuadTree node.
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def trav(i: int, j: int, dist: int) -> 'Node':
            if dist == 1:
                return Node(grid[i][j], True, None, None, None, None)

            isLeaf = True
            val = grid[i][j]
            for r in range(i, i + dist):
                for c in range(j, j + dist):
                    if grid[r][c] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break

            if isLeaf:
                return Node(val, True, None, None, None, None)

            newDist = dist // 2
            topLeft = trav(i, j, newDist)
            topRight = trav(i, j + newDist, newDist)
            bottomLeft = trav(i + newDist, j, newDist)
            bottomRight = trav(i + newDist, j + newDist, newDist)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return trav(0, 0, n)

# TC: O(n^2 * logn)
# SC: O(logn + n^2) -> logn for recursion stack and n^2 for the quad tree nodes
