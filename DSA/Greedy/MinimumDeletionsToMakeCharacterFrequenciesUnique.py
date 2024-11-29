from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freqMap = Counter(s)
        freqMap = dict(sorted(freqMap.items(), key=lambda x: x[1], reverse=True))
        nums = set()
        removals = 0

        for v in freqMap.values():
            if v not in nums:
                nums.add(v)
            else:
                newF = v
                while newF in nums:
                    newF -= 1
                if newF:
                    nums.add(newF)
                removals += (v - newF)
        return removals

# TC: O(nlogn)
# SC: O(n)