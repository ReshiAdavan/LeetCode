class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Combine the two arrays into a single sorted array
        merged = sorted(nums1 + nums2)
        
        # Calculate the length of the merged array
        length = len(merged)
        
        # Check if the length is odd or even
        if length % 2 == 0:
            # If the length is even, return the average of the middle two elements
            mid = length // 2
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            # If the length is odd, return the middle element
            mid = length // 2
            return merged[mid]
        
# Beats 81.96% python submissions in runtime
# Beats 17.51% python submissions in memory usage
