from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0: 1}
        summ = 0
        res = 0
        for n in nums:
            summ += n
            if summ - k in table:
                res += table[summ - k]
            if summ in table:
                table[summ] += 1
            else:
                table[summ] = 1
        return res
    
# TC: O(n)
# SC: O(n)
