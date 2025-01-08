class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        
        if length % 2 == 0:
            mid = length // 2
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            mid = length // 2
            return merged[mid]
        
# Beats 81.96% python submissions in runtime
# Beats 17.51% python submissions in memory usage
