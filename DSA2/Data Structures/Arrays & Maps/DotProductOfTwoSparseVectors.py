from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = {}
        for i, n in enumerate(nums):
            if n != 0: 
                self.array[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, n in self.array.items():
            if i in vec.array:
                res += (n * vec.array[i])
        return res
    
# TC: O(n)
# SC: O(n)
