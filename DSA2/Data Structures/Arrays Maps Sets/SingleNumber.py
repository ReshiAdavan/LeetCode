from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k

# TC: O(n)
# SC: O(n)
