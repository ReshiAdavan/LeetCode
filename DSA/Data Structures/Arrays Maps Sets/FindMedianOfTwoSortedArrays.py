from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        
        if length % 2 == 0:
            mid = length // 2
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            mid = length // 2
            return merged[mid]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m
        while True:
            partition1 = (left + right) // 2
            partition2 = half - partition1

            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

# TC: O(log(min(m, n)))
# SC: O(1)
