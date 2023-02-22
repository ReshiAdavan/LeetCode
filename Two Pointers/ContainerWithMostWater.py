class Solution(object):
    def maxArea(self, height):
        l, r, A = 0, len(height) - 1, 0
        while l < r:
            A = max(A, (r - l) * (min(height[l], height[r])))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return A

# Beats 82.77% python submissions in runtime
# Beats 77.34% python submissions in memory usage  