from typing import List
from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter()
        MOD = 10**9 + 7
        total = 0

        for meal in deliciousness:
            for exp in range(22):
                target = (1 << exp) - meal
                if target in counter:
                    total += counter[target]
            counter[meal] += 1
        return total % MOD

# TC: O(22n)
# SC: O(n)

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter()
        MOD = 10**9 + 7
        total = 0

        maxi = 2 * max(deliciousness)
        upperBoundExp = 0
        power = 1

        while power <= maxi:
            upperBoundExp += 1
            power <<= 1

        for meal in deliciousness:
            for exp in range(upperBoundExp + 1):
                target = (1 << exp) - meal
                if target in counter:
                    total += counter[target]
            counter[meal] += 1
        return total % MOD

## log(max(n)) <= 22 
# TC: O(log(max(n)) * n)
# SC: O(n)
