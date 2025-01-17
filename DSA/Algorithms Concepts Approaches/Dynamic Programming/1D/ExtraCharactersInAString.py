from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        cache = {}

        def memo(i):
            if i >= len(s):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = 1 + memo(i + 1)  # Take current char as extra
            for word in dictionary:
                if s[i:i + len(word)] == word:
                    cache[i] = min(cache[i], memo(i + len(word)))
            return cache[i]

        return memo(0)

# N = len(s), M = len(dictionary)
# TC: O(N * M)
# SC: O(N)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = [0] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for word in dictionary:
                if s[i:i + len(word)] == word:
                    dp[i] = min(dp[i], dp[i + len(word)])

        return dp[0]

# TC: O(N * M)
# SC: O(N)
