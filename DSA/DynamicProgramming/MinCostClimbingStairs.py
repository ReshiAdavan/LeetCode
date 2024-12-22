class Solution(object):
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

# Beats 89.44% python submissions in runtime
# Beats 76.50% python submissions in memory usage