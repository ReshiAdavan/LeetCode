from typing import List

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxi = damage.index(max(damage))
        damage[maxi] = max(0, damage[maxi] - armor)
        return sum(damage) + 1

# TC: O(N)
# SC: O(1)
