from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        res = []

        for char in order:
            if char in counter:
                res.append(char * counter[char])
                counter[char] = 0

        for char, freq in counter.items():
            if freq > 0:
                res.append(char * freq)
                counter[char] = 0
        return "".join(res)

# TC: O(s + o)
# SC: O(s)
