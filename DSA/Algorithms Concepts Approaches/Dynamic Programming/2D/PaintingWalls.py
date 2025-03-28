class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        dp = {}
        
        def dfs(i, remain):
            if remain <= 0: 
                return 0
            if i == len(cost):
                return float("inf")
            if (i, remain) in dp:
                return dp[(i, remain)]
            
            # two decisions (paint or dont)
            paint = cost[i] + dfs(i + 1, remain - 1 - time[i]) 
            skip = dfs(i + 1, remain)
            dp[(i, remain)] = min(paint, skip)
            return dp[(i, remain)]
        
        return dfs(0, len(cost))

#  Beats 14.95% of users with Python3 in runtime
#  Beats 52.45% of users with Python3 in memory

