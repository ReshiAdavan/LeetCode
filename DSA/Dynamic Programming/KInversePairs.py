class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        cache = {}

        def dfs(n, k) -> int:
            if k < 0:
                return 0
            if n == 0:
                return k == 0
            if (n, k) in cache:
                return cache[(n, k)]
            
            res = 0
            for i in range(n):
                res += dfs(n - 1, k - i) % MOD
            cache[(n, k)] = res
            return cache[(n, k)]

        return dfs(n, k)

## Its a valid solution but gets a "TIME LIMIT EXCEEDED" on LeetCode
# Time Complexity: O(n * n * k)
# Space Complexity: O(n * k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for N in range(1, n + 1):
            nextDP = [0] * (k + 1)
            for K in range(0, k + 1):
                for pairs in range(N):
                    if K - pairs >= 0:
                        nextDP[K] = (nextDP[K] + dp[K - pairs]) % MOD
            dp = nextDP
        return dp[K]
    
## Another valid solution but gets a "TIME LIMIT EXCEEDED" on LeetCode
# Time Complexity: O(n * n * k)
# Space Complexity: O(k)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for N in range(1, n + 1):
            nextDP = [0] * (k + 1)
            total = 0
            for K in range(0, k + 1):
                if K >= N:
                    total -= dp[K - N]
                total = (total + dp[K]) % MOD
                nextDP[K] = total
            dp = nextDP
        return dp[k]

# Time Complexity: O(n * k)
# Space Complexity: O(k)
# Beats 99.33% of python users in runtime
# Beats 99.67% of python users in memory usage
