class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        first = {}
        last = {}
        
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        
        for char in first:
            if first[char] < last[char]:
                middle_chars = set(s[first[char] + 1:last[char]])
                result += len(middle_chars)
        
        return result

# TC: O(26n)
# SC: O(26)
