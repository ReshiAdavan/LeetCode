from collections import deque

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if target == 0:
            return True

        v = set((0, 0))
        q = deque([(0, 0)])

        while q:
            i, j = q.popleft()
            if i == target or j == target or i + j == target:
                return True

            states = [
                (x, j),
                (i, y),
                (0, j),
                (i, 0),
                (min(i + j, x), j - min(i + j, x)),
                (i - min(i + j, x), min(i + j, x))
            ]

            for new_state in states:
                if new_state not in v:
                    v.add(new_state)
                    q.append(new_state)

        return False

# Time Complexity: O((x + 1) * (y + 1))
# Space Complexity: O((x + 1) * (y + 1))

import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target: 
            return False
        if target == 0: 
            return True
        return target % math.gcd(x, y) == 0

# Time Complexity: O(log(min(x,y)))
# Space Complexity: O(1)

### Since the water and jug problem can be represented as a linear combination (i.e. ax + by = target)
### And by number theory, any number represented via linear combination must be a mulitple of the GCD(x, y)
### Then target must be divisble by GCD(x, y), otherwise impossible and cant rep. linear combination
