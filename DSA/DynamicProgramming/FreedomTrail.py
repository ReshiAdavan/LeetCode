from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}
        ring_map = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_map[ch].append(i)

        def dfs(i, j): 
            if j == len(key):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            min_steps = float("inf")

            for idx in ring_map[key[j]]:
                dist = abs(i - idx)
                min_dist = min(dist, len(ring) - dist) 
                steps = 1 + min_dist + dfs(idx, j + 1)
                min_steps = min(min_steps, steps)
            
            cache[(i, j)] = min_steps
            return cache[(i, j)]

        return dfs(0, 0)

# Time Complexity: O(R^2 * K)
# Space Complexity: O(R^2)
# Beats 64.35% of python users in runtime
# Beats 94.35% of python users in memory usage

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        
        for k in reversed(range(len(key))):
            next_dp = [float("inf")] * len(ring)
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        dist = abs(r - i) 
                        min_dist = min(dist, len(ring) - dist)
                        next_dp[r] = min(next_dp[r], min_dist + 1 + dp[i])
            dp = next_dp
        return dp[0]

# Time Complexity: O(R^2 * K)
# Space Complexity: O(R)
# Beats 7.95% of python users in runtime
# Beats 100.00% of python users in memory usage

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        ring_map = defaultdict(list)
        for i, ch in enumerate(ring):
            ring_map[ch].append(i)
        
        for k in reversed(range(len(key))):
            next_dp = [float("inf")] * len(ring)
            for r in range(len(ring)):
                for i in ring_map[key[k]]:
                    dist = abs(r - i) 
                    min_dist = min(dist, len(ring) - dist)
                    next_dp[r] = min(next_dp[r], min_dist + 1 + dp[i])
            dp = next_dp
        return dp[0]


# Time Complexity: O(R^2 * K)
# Space Complexity: O(R)
# Beats 12.47% of python users in runtime
# Beats 88.82% of python users in memory usage
