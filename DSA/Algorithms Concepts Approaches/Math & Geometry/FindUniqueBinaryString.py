from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        newNums = set()
        for i in nums:
            newNums.add(int(i, 2))

        for i in range(0, 2 ** n):
            if i not in newNums:
                binary = bin(i)[2:]
                padded = binary.zfill(n)
                return padded

# TC: O(n^2 + 2^n); str -> int, check every num up to 2^n
# SC: O(n^2); set of n nums where each num has n bits

## Cantors diagonal argument
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        buildStr = []
        for i in range(len(nums)):
            buildStr.append("0" if nums[i][i] == "1" else "1")
        return "".join(buildStr)

# TC: O(n)
# SC: O(n)
