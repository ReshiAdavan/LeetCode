class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        return (nums1[n//2-1]/2.0+nums1[n//2]/2.0, nums1[n//2])[n % 2] if n else None        

## Lazy Approach
# Beats 71.38% python submissions in runtime
# Beats 74.05% python submissions in memory usage  
        