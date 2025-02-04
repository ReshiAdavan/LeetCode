from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cache = {}
        MOD = 10**9 + 7

        def memo(rollsLeft, lastNum, consecRolls):
            if rollsLeft == 0:
                return 1
            if (rollsLeft, lastNum, consecRolls) in cache:
                return cache[(rollsLeft, lastNum, consecRolls)]

            total = 0
            for i in range(6):
                if i == lastNum:
                    if consecRolls < rollMax[i]:
                        total += memo(rollsLeft - 1, lastNum, consecRolls + 1) % MOD
                else:
                    total += memo(rollsLeft - 1, i, 1) % MOD
            cache[(rollsLeft, lastNum, consecRolls)] = total % MOD
            return cache[(rollsLeft, lastNum, consecRolls)]
        return memo(n, -1, 0)

# TC: O(n * 6 * max(rollMax))
# SC: O(n * 6 * max(rollMax))
