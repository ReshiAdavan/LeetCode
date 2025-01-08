class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def memo(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i >= len(s):
                return all(char == '*' for char in p[j:])
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == p[j] or p[j] == '?':
                cache[(i, j)] = memo(i + 1, j + 1)
            elif p[j] == "*":
                cache[(i, j)] = memo(i, j + 1) or memo(i + 1, j)
            else:
                cache[(i, j)] = False
            return cache[(i, j)]
        
        return memo(0, 0)

# TC: O(s*p)
# SC: O(s*p)

