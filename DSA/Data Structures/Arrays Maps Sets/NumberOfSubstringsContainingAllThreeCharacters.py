class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        charSeen = {}

        for i in range(len(s)):
            charSeen[s[i]] = i
            if 'a' in charSeen and 'b' in charSeen and 'c' in charSeen:
                minPos = min(charSeen['a'], charSeen['b'], charSeen['c'])
                count += (minPos + 1)
        return count

# TC: O(N)
# SC: O(N)
