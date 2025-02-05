class FenwickTree:
    """
    A Fenwick Tree (Binary Indexed Tree) implementation that supports:
    1. Point updates - Update a single value in O(log n) time
    2. Range queries - Get sum from index 1 to x in O(log n) time
    """
    def __init__(self, size):
        """
        Size + 1 because Fenwick Tree is 1-indexed
        Index 0 simplifies the binary operations
        """
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """
        Add delta to value at given index.
        Also update all responsible range sums
        """
        while index <= self.size:
            self.tree[index] += delta
            # index & (-index) isolates the least significant set bit
            index += index & (-index)
        
    def query(self, index: int) -> int:
        """
        Get sum of all values from index 1 to given index.
        """
        total = 0
        while index > 0:
            total += self.tree[index]
                # Remove least significant set bit to move to parent
            index -= index & (-index)
        return total

from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        maxi = max(instructions)
        bit = FenwickTree(maxi)
        cost = 0

        for i, num in enumerate(instructions):
            lessCount = bit.query(num - 1)
            greaterCount = i - bit.query(num)
            cost = (cost + min(lessCount, greaterCount)) % MOD
            bit.update(num, 1)
        return cost

# TC: O(n * log n)
# SC: O(n)
