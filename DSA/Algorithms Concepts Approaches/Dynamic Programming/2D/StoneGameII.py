from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        suffixSums = piles[::]
        for i in range(len(piles) - 2, -1, -1):
            suffixSums[i] += suffixSums[i + 1]

        def memo(i, m, turn):
            if i >= len(piles):
                return 0
            if (i, m, turn) in cache:
                return cache[(i, m, turn)]
            if i + 2 * m >= len(piles):
                return suffixSums[i] if turn else 0

            if turn:
                alice = 0
                for x in range(1, 2 * m + 1):
                    if i + x > len(piles):
                        break
                    curSum = suffixSums[i] - (suffixSums[i + x] if i + x < len(piles) else 0)
                    alice = max(alice, curSum + memo(i + x, max(m, x), False))
                cache[(i, m, turn)] = alice
                return alice
            else:
                alice = float('inf')
                for x in range(1, 2 * m + 1):
                    if i + x > len(piles):
                        break
                    alice = min(alice, memo(i + x, max(m, x), True))
                cache[(i, m, turn)] = alice
                return alice

        return memo(0, 1, True)
    
# TC: O(n^2)
# SC: O(n^2)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        suffixes = piles[::]
        for i in range(len(piles) - 2, -1, -1):
            suffixes[i] += suffixes[i + 1]

        def memo(i: int, m: int) -> int:
            if i >= len(piles):
                return 0
            if i + 2 * m >= len(piles):
                return suffixes[i]
            if (i, m) in cache:
                return cache[(i, m)]

            mini = float('inf')
            for x in range(1, 2 * m + 1):
                if i + x > len(piles):
                    break
                mini = min(mini, memo(i + x, max(m, x)))

            cache[(i, m)] = suffixes[i] - mini
            return cache[(i, m)]

        return memo(0, 1)

## Instead of tracking alice and bob's scores, we just track the opponents and subtract from the entire sum.
## Since bob plays optimally, we can just subtract his score from the total sum to get alice's score.
# TC: O(n^2)
# SC: O(n^2)