from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        heights = [0] * COLS
        maxi = 0

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxi = max(maxi, self.largestRectangleArea(heights))
        return maxi

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxi = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxi = max(maxi, height * width)
            stack.append(i)

        heights.pop()
        return maxi

# TC: O(n*m)
# SC: O(m)
