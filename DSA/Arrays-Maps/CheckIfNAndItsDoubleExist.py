from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()

        for n in arr:
            if n / 2 in nums or 2 * n in nums:
                return True
            nums.add(n)
        return False


# TC: O(n)
# SC: O(n)
