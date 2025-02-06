from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrLen = len(arr)
        counter = Counter(arr)

        buckets = [0] * (arrLen + 1)
        for freq in counter.values():
            buckets[freq] += 1

        newLen = 0
        removals = 0

        for i in range(len(buckets) - 1, 0, -1):
            while buckets[i]:
                if newLen >= arrLen // 2:
                    return removals
                removals += 1
                newLen += i
                buckets[i] -= 1
        return removals

# TC: O(n)
# SC: O(n)
