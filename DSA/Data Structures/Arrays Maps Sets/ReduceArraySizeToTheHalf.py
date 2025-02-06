from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrLen = len(arr)
        counter = sorted(Counter(arr).items(), key=lambda x: x[1], reverse=True)
        newLen = 0
        removals = 0

        for _, freq in counter:
            newLen += freq
            removals += 1
            if newLen >= arrLen // 2:
                return removals
                
# TC: O(nlogn)
# SC: O(n)
