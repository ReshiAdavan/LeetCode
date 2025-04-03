from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        lookup = {v: i for i, v in enumerate(arr)}
        maxi = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                length = 2

                while a + b in lookup and lookup[a + b] > j:
                    c = a + b
                    a, b = b, c
                    length += 1

                if length >= 3:
                    maxi = max(maxi, length)
        return maxi

# Let m rep. len(longest Fibonacci subsequence)
# TC: O(n * n * m)
# SC: O(n)
