class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if s[i] == "1":
                continue

            for j in range(i + minJump, min(i + maxJump + 1, n)):
                if s[j] == '0':
                    dp[j] = True

        return dp[-1]

## TLE
# TC: O(N * (maxJump - minJump))
# SC: O(N)
