from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                prevIdx, prevHeight = stack.pop()
                area = (index - prevIdx) * prevHeight
                maxArea = max(maxArea, area)
                start = prevIdx
            stack.append([start, height])

        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)
        return maxArea

# TC: O(n)
# SC: O(n) 
