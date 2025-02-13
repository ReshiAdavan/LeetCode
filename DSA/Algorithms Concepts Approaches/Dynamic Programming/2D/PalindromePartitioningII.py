class Solution:
    def minCut(self, s: str) -> int:
        # identify palindromes
        cache = {}

        def IP(i, j):
            if i > j:
                return
            if j >= len(s):
                return
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i: j + 1] == s[i: j + 1][::-1]:
                cache[(i, j)] = 1
            else:
                cache[(i, j)] = 0
            IP(i, j + 1)
            IP(i + 1, j)

        IP(0, 0)

        # cut based on palindromes
        cache2 = {}

        def cuts(i):
            if i < 0:
                return -1
            if i == 0:
                return 0
            if i in cache2:
                return cache2[i]

            mini = float("inf")
            for j in range(i + 1):
                if cache.get((j, i), 0):
                    mini = min(mini, 1 + cuts(j - 1)) if j != 0 else 0
            cache2[i] = mini
            return cache2[i]

        return cuts(len(s) - 1)

# TC: O(N^2)
# SC: O(N^2)
