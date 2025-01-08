class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s), 2):
            if s[i] != s[i - 1]:
                changes += 1
        return changes

# TC: O(n) 
# SC: O(1)
