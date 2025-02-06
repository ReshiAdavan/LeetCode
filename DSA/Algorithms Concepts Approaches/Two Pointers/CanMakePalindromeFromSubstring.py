from collections import Counter
from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        solns = []
        for left, right, k in queries:
            solns.append(
                self.minSwapsToPali(s[left: right + 1]) <= k
            )
        return solns

    def minSwapsToPali(self, s: str) -> int:
        counter = Counter(s)
        oddCount = sum(1 for count in counter.values() if count % 2)
        return oddCount // 2

## TLE
# TC: O(N * Q)
# SC: O(N)
