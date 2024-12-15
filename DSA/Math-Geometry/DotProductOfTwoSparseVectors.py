from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for num1, num2 in zip(self.array, vec.array):
            res += (num1 * num2)
        return res

# TC: O(n)
# SC: O(1)
