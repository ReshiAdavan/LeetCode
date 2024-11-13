from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = Counter(s)
        for idx, ch in enumerate(s):
            if freqMap[ch] == 1:
                return idx
        return -1
    
# TC: O(n)
# SC: O(n)
