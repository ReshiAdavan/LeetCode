from typing import List

class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# Beats 38.25% python submissions in runtime
# Beats 73.71% python submissions in memory usage

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLefts = [0] * n
        maxRights = [0] * n

        # maxLefts
        maxLefts[0] = height[0]
        for i in range(1, n):
            maxLefts[i] = max(maxLefts[i - 1], height[i])

        # maxRights
        maxRights[-1] = height[-1]
        for j in range(n - 2, -1, -1):
            maxRights[j] = max(maxRights[j + 1], height[j])

        res = 0
        for k in range(n):
            res += max(0, min(maxLefts[k], maxRights[k]) - height[k])
        return res

# TC: O(n)
# SC: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        left, right = 0, len(height) - 1
        maxiLeft, maxiRight = height[0], height[-1]

        while left < right:
            if maxiLeft < maxiRight:
                left += 1
                maxiLeft = max(maxiLeft, height[left])
                res += max(0, maxiLeft - height[left])
            else:
                right -= 1
                maxiRight = max(maxiRight, height[right])
                res += max(0, maxiRight - height[right])
        return res

# TC: O(n)
# SC: O(1)
