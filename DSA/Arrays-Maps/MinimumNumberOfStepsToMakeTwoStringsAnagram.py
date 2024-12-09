from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)

        res = 0
        for char, freq in sCounter.items():
            f = tCounter[char]
            if freq > f:
                res += (freq - f)
        return res

# TC: O(s + t)
# SC: O(s + t)
