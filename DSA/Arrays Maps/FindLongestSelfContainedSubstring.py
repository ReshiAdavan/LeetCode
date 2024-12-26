class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        first_pos = {}
        last_pos = {}
        
        for i, char in enumerate(s):
            if char not in first_pos:
                first_pos[char] = i
            last_pos[char] = i
            
        max_length = -1
        
        for i in range(n):
            for j in range(i, n):
                valid = True
                
                for k in range(i, j + 1):
                    char = s[k]
                    if first_pos[char] < i or last_pos[char] > j:
                        valid = False
                        break
                
                if valid and j - i + 1 < n:
                    max_length = max(max_length, j - i + 1)
        
        return max_length

## Pure Bruteforce (TLE) 
# TC: O(N^3)
# SC: O(N)

from collections import defaultdict

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        # Store the first and last occurrence of each character
        intervals = defaultdict(list)
        for i, c in enumerate(s):
            if c in intervals:
                intervals[c][1] = i
            else:
                intervals[c] = [i, i]  # [first_pos, last_pos]

        n = len(s)
        res = 0

        for c in intervals:
            leftend, rightend = intervals[c]

            for i in range(leftend, n):
                if intervals[s[i]][0] < leftend:
                    break

                rightend = max(rightend, intervals[s[i]][1])

                if i == rightend and rightend - leftend + 1 != n:
                    res = max(res, rightend - leftend + 1)

        return res if res else -1

# TC: O(26*N)
# SC: O(N)
