class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        cache = [[-1] * 3 for _ in range(len(corridor))]

        def dfs(i: int, s: int) -> int:
            if i >= len(corridor):
                return 1 if s == 2 else 0

            if cache[i][s] != -1:
                return cache[i][s]

            res = 0 
            if s == 2:
                if corridor[i] == "S":
                    res = dfs(i + 1, 1)
                else:
                    res = dfs(i + 1, 0) + dfs(i + 1, s)
            else:
                if corridor[i] == "S":
                    res = dfs(i + 1, s + 1)
                else:
                    res = dfs(i + 1, s)
            cache[i][s] = res % MOD
            return cache[i][s]

        return dfs(0, 0)
    
# Time Complexity: O(3*N)
# Space Complexity: O(3*N)
# Beats 5.65% of python users in runtime
# Beats 6.52% of python users in memory usage

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seats = []
        for i, c in enumerate(corridor):
            if c == "S":
                seats.append(i)
        
        length = len(seats)
        if length < 2 or length % 2 == 1:
            return 0
        
        res = 1
        for i in range(1, length - 1, 2):
            res = (res * (seats[i + 1] - seats[i])) % mod
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(N)
# Beats 91.74% of python users in runtime
# Beats 38.70% of python users in memory usage

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seatCount = 0
        ways = 1
        lastSeat = -1
        
        for i, c in enumerate(corridor):
            if c == 'S':
                seatCount += 1
                if seatCount > 2 and seatCount % 2 == 1:
                    ways = (ways * (i - lastSeat)) % mod
                lastSeat = i

        if seatCount < 2 or seatCount % 2 == 1:
            return 0

        return ways

# Time Complexity: O(N)
# Space Complexity: O(1)
# Beats 64.35% of python users in runtime
# Beats 94.35% of python users in memory usage
