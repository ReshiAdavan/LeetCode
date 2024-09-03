class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        sideLen = sum(matchsticks)
        if sideLen % 4 != 0:
            return False

        sideLen /= 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)
        
        def backtrack(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == sideLen
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= sideLen:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]

                if sides[i] == 0:
                    break
            
            return False
            
        return backtrack(0)

# Beats 72.84% of users with Python3 in runtime 
# Beats 51.35% of users with Python3 in memory
