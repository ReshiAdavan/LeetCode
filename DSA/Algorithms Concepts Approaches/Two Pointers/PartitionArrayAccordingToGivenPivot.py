from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThanPivot = []
        equalToPivot = []
        greaterThanPivot = []

        for n in nums:
            if n < pivot:
                lessThanPivot.append(n)
            elif n > pivot:
                greaterThanPivot.append(n)
            else:
                equalToPivot.append(n)

        return lessThanPivot + equalToPivot + greaterThanPivot

# TC: O(N)
# SC: O(N)
