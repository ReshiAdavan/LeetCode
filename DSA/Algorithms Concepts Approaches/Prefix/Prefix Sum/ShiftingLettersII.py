from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftsPerChar = [0] * (len(s) + 1)  # extra space in array for last index 

        # mark start and end (inclusive, exclusive)
        for start, end, direction in shifts:
            change = 1 if direction else -1
            shiftsPerChar[start] += change
            shiftsPerChar[end + 1] -= change

        # prefix sum efficiently updates every position with every correct # of shifts
        # instead of having to update intervals on array per interval
        for i in range(1, len(s)):
            shiftsPerChar[i] += shiftsPerChar[i - 1]

        result = []
        for i in range(len(s)):
            # bring to domain 0 - 26, add shifts, make sure it stays in range, then bring 
            # back to lowercase alphabetical domain
            newCh = chr((ord(s[i]) - ord('a') + shiftsPerChar[i]) % 26 + ord('a'))
            result.append(newCh)
        return ''.join(result)

# Let S represent size of string, Q represent size of shifts
# TC: O(Q + S + S) -> O(Q + S)
# SC: O(S)
