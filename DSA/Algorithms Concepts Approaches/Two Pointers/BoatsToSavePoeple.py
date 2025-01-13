from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if l != r and people[l] + people[r] <= limit:
                l, r = l + 1, r - 1
            else:
                r -= 1
            boats += 1
        return boats

# TC: O(NlogN)
# SC: O(1)
