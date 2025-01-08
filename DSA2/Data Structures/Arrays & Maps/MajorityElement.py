from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqCounter = Counter(nums)
        maxiFreq = 0
        majorityElem = ""

        for n, f in freqCounter.items():
            if maxiFreq < f:
                maxiFreq = f
                majorityElem = n
        return majorityElem

# TC: O(n)
# SC: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0

        for n in nums:
            if not majority:
                res = n

            if n == res:
                majority += 1
            else:
                majority -= 1

        return res

# TC: O(n)
# SC: O(1)
