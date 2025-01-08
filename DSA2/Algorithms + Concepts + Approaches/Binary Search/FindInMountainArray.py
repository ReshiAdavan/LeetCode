"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""

class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # Find peak
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if mountainArr.get(middle) < mountainArr.get(middle + 1):
                left = middle + 1
            else:
                right = middle - 1
        peak = left

        # (0 to peak)
        left, right = 0, peak
        while left <= right:
            middle = (left + right) // 2
            val = mountainArr.get(middle)
            if val == target:
                return middle
            elif val < target:
                left = middle + 1
            else:
                right = middle - 1

        # (peak + 1 to n - 1)
        left, right = peak + 1, n - 1
        while left <= right:
            middle = (left + right) // 2
            val = mountainArr.get(middle)
            if val == target:
                return middle
            elif val < target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

# TC: O(log(n))
# SC: O(1)
