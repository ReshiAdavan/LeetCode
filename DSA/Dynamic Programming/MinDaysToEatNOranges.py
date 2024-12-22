class Solution:
    def minDays(self, n: int) -> int:
        cache = {0 : 0, 1 : 1}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            consumeHalf = (i % 2) + dfs(i // 2)
            consumeTwoThirds = (i % 3) + dfs(i // 3)
            cache[i] = 1 + min(consumeHalf, consumeTwoThirds)
            return cache[i]

        return dfs(n)

# Time Complexity: O(N)
# Space Complexity: O(N)
# Beats 96.98% of python users in runtime
# Beats 41.69% of python users in memory usage
