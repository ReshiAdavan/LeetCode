from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        totalLen = sum(ribbons)
        if totalLen < k:
            return 0

        lower, upper = 1, min(max(ribbons), totalLen)
        res = 0

        def foo(middle):
            total = 0
            for r in ribbons:
                total += (r // middle)
            return (total >= k)

        while lower <= upper:
            middle = (lower + upper) // 2

            if foo(middle):
                res = middle
                lower = middle + 1
            else:
                upper = middle - 1
        return res

# M rep. the minumum length of the maximum ribbon size or the total length of all ribbons
# TC: O(N * log(M)))
# SC: O(1)
