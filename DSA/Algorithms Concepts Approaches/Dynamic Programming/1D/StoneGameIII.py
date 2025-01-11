from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> int:
        cache = {}
        suffixes = stoneValue[::]
        for i in range(len(stoneValue) - 2, -1, -1):
            suffixes[i] += suffixes[i + 1]

        def memo(i):
            if i >= len(stoneValue):
                return 0
            if i in cache:
                return cache[i]

            bob = float("inf")
            for j in range(3):
                if i + j < len(stoneValue):
                    score = memo(i + j + 1)
                    bob = min(bob, score)

            cache[i] = suffixes[i] - bob
            return cache[i]

        alice = memo(0)
        bob = suffixes[0] - alice

        if alice > bob:
            return "Alice"
        if bob > alice:
            return "Bob"
        return "Tie"

# TC: O(n)
# SC: O(n)