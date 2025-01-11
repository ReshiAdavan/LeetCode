from typing import List
from collections import deque

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        d = deque()

        for p in piles:
            d.append(p)

        alice = 0
        bob = 0
        count = 0

        while d:
            if count % 2 == 0:
                if d[0] > d[-1]:
                    alice += d.popleft()
                else:
                    alice += d.pop()
            else:
                if d[0] > d[-1]:
                    bob += d.popleft()
                else:
                    bob += d.pop()

        return alice > bob

# TC: O(n)
# SC: O(n)

# Alice can choose either only even or only odd stones, and if she chooses optimally, 
# then she will always win. Hence we dont need to simulate that optimal iteration and immediately return True.

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
