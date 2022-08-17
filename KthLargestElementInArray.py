import heapq  # Import only necessary for syntatical purposes and not for LC submissions

# Solution 1
class Solution(object):
    def findKthLargest(self, nums, k):
        if len(nums) == 1: 
            return nums[0] 
        nums.sort(reverse = True)
        return nums[k - 1]

# Beats 47.24% python submissions in runtime
# Beats 30.42% python submissions in memory usage  

# Solution 2
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)
        resultList = heapq.nsmallest(k, nums)
        return -1 * resultList[k-1]

# Beats 33.93% python submissions in runtime
# Beats 10.85% python submissions in memory usage  

# Solution 3
class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

# Beats 29.27% python submissions in runtime
# Beats 37.89% python submissions in memory usage  
