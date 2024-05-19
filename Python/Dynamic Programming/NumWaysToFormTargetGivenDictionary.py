class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9  + 7
        T = len(target)
        W = len(words[0])

        # precompute the aamount of common characters across words 
        countDict = defaultdict(int)
        for w in words:
            for i, c in enumerate(w):
                countDict[(i, c)] += 1

        dp = {}
        # i is the index for target and k is the index for words[j]
        def dfs(i, k):
            if i >= T:
                return 1
            if k >= W:
                return 0
            if (i, k) in dp:
                return dp[(i, k)]

            c = target[i]
            # skipping character
            dp[(i, k)] = dfs(i, k + 1)
            # choosing matching character
            dp[(i, k)] += countDict[(k, c)] * dfs(i + 1, k + 1)
            return dp[(i, k)]

        return dfs(0, 0) % MOD
    
# Beats 10.94% of users with Python3 in runtime
# Beats 5.20% of users with Python3 in memory