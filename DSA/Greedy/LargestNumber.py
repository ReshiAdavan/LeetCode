from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if int(n1 + n2) > int(n2 + n1):
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"
    
        return "".join(nums)

# TC: O(nlogn)
# SC: O(n)

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = [str(ele) for ele in nums]
        numbers.sort(key=lambda x: x*10, reverse=True)

        if numbers[0] == "0":
            return "0"
    
        return "".join(numbers)

## This only works because the largest number is 10^9 and `key=lambda x: x*10` bounds every string to 10 digits
# TC: O(nlogn)
# SC: O(n)