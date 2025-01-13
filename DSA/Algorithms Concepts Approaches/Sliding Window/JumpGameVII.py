class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        count = 0

        for i in range(1, n):
            # At any position i, jump between [i + minJump, i + maxJump]
            if i >= minJump:
                count += dp[i - minJump]
            if i > maxJump:
                count -= dp[i - maxJump - 1]

            dp[i] = count > 0 and s[i] == '0'

        return dp[-1]

# TC: O(N)
# SC: O(N)