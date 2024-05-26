class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S = len(s)
        dp = [False] * (S + 1)
        dp[-1] = True
        for i in range(S - 1, -1, -1):
            for w in wordDict:
                if s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

# Beats 80.36% of users with Python3 in runtime
# Beats 93.86% of users with Python3 in memory