from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        def strPattern(s: str) -> str:
            if len(s) <= 1:
                return ""

            pattern = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                pattern.append(diff)

            return tuple(pattern)

        for s in strings:
            pattern = strPattern(s)
            groupings[pattern].append(s)

        return list(groupings.values())

# N rep. # of strings. K rep. avg. length of strings
# TC: O(N * K)
# SC: O(N * K)
