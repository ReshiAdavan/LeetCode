class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def memo(p1, p2):
            if p1 >= len(text1) and p2 >= len(text2):
                return 0
            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            if (p1, p2) in cache:
                return cache[(p1, p2)]

            if text1[p1] == text2[p2]:
                cache[(p1, p2)] = 1 + memo(p1 + 1, p2 + 1)
            else:
                cache[(p1, p2)] = max(memo(p1 + 1, p2), memo(p1, p2 + 1))
            return cache[(p1, p2)]

        return memo(0, 0)

# TC: O(n*m)
# SC: O(n*m)

