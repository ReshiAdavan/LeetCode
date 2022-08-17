import heapq  # Import only necessary for syntatical purposes and not for LC submissions

class Solution(object):
    def kClosest(self, points, k):
        p = []
        for x, y in points:
            d = sqrt(x*x + y*y)
            p.append([d, x, y])
        ans = []
        heapq.heapify(p)
        for i in range(k): 
            d, x, y = heapq.heappop(p)
            ans.append([x, y])
        return ans

# Beats 93.27% python submissions in runtime
# Beats 11.64% python submissions in memory usage  
