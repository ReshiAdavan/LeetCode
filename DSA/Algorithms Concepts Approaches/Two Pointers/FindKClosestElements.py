from collections import deque
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        # binary search
        insertPoint = 0
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= x:
                right = mid
                insertPoint = mid
            else:
                left = mid + 1
                insertPoint = left

        # two pointer and expand out from insertion point
        res = deque()
        left, right = insertPoint - 1, insertPoint
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.appendleft(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.appendleft(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
        return list(res)

# TC: O(logn + k)
# SC: O(k)
