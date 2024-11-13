from typing import List

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# Beats 36.27% python submissions in runtime
# Beats 24.75% python submissions in memory usage

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        maxi = 0
        for n in nums:
            if n not in table:
                left = table.get(n - 1, 0)
                right = table.get(n + 1, 0)

                curr_len = 1 + left + right
                maxi = max(curr_len, maxi)

                table[n] = curr_len
                table[n - left] = curr_len
                table[n + right] = curr_len
        return maxi
    
# TC: O(n)
# SC: O(n)