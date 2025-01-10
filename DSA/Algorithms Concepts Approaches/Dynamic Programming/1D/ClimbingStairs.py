class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1 
        if n == 2: return 2
        ways = [0 for i in range(n)]
        ways[n - 1], ways[n - 2] = 1, 2
        i = n - 3
        while i >= 0: 
            ways[i] = ways[i + 1] + ways[i + 2]
            i -= 1 
        return ways[0]
        
# Beats 96.07% python submissions in runtime
# Beats 63.09% python submissions in memory usage

