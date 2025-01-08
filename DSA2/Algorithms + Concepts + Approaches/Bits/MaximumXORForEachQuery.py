from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        preComputedXORValues = [nums[0]]
        xorValue = nums[0]
        for n in nums[1:]:
            xorValue ^= n
            preComputedXORValues.append(xorValue)
        preComputedXORValues.reverse()

        res = []
        mask = 2**maximumBit - 1
        for xorVal in preComputedXORValues:
            k = xorVal ^ mask
            res.append(k)
        return res
    

## N solutions per query where the size of the integer N is M bits
# TC: O(N * M) 
# SC: O(N * M)
