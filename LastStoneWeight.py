import heapq  # Import only necessary for syntatical purposes and not for LC submissions

class Solution(object):
    def lastStoneWeight(self, stones):
        if len(stones) == 1:
            return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:  
            r1 = heapq.heappop(stones)
            r2 = heapq.heappop(stones)
            if r1 != r2: 
                heapq.heappush(stones, r1 - r2)
        return -1 * stones[0] if stones else 0

# Beats 72.09% python submissions in runtime
# Beats 77.19% python submissions in memory usage  
