from typing import List
from math import gcd

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maxi = max(nums)
        nums = set(nums)
        count = 0
        
        for i in range(1, maxi + 1):
            x = 0
            for m in range(i, maxi + 1, i):
                if m in nums:
                    x = gcd(x, m)
            
            if x == i:
                count += 1
        return count

# TC: O(maxi(nums) * log(maxi(nums)))
# SC: O(n)
