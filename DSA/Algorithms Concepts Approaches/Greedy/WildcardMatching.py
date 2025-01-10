class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        star_index = -1
        match = 0

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_index = j
                match = i
                j += 1
            elif star_index != -1:
                j = star_index + 1
                match += 1
                i = match
            else:
                return False

        # Check remaining characters in p
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)

# TC: O(s + p)
# SC: O(1)
