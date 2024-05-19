class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        courseMap = {i: [] for i in range(1, n + 1)}
        for prevCourse, nextCourse in relations:
            courseMap[nextCourse].append(prevCourse)
        dp = {}

        def dfs(src):
            if len(courseMap[src]) <= 0:
                dp[src] = time[src - 1]
                return dp[src]
            if src in dp:
                return dp[src]

            maxi = 0
            for n in courseMap[src]:
                maxi = max(maxi, dfs(n))
            dp[src] = maxi + time[src - 1]
            return dp[src]

        for i in range(1, n + 1):
            dfs(i)

        return max(dp.values())

# Beats 81.04% of users with Python3 in runtime
# Beats 17.97% of users with Python3 in memory