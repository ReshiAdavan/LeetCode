from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        requiredSum = mean * (m + n) - sum(rolls)
        if requiredSum < n or requiredSum > 6 * n:
            return []

        # evenly distribute n rolls across required sum
        print(requiredSum, n)
        base = requiredSum // n
        R = requiredSum % n

        res = []
        for i in range(n):
            if i < R:
                res.append(base + 1)
            else:
                res.append(base)
        return res

# TC: O(n)
# SC: O(1)
