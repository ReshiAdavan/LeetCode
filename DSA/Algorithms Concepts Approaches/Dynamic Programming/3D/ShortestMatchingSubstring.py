class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        optimized_p = []
        for char in p:
            if char == '*' and optimized_p and optimized_p[-1] == '*':
                continue
            optimized_p.append(char)
        p = ''.join(optimized_p)

        cache = {}
        def memo(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j == len(p):
                return 0
            if i == len(s):
                return 0 if all(p[k] == '*' for k in range(j, len(p))) else float('inf')

            result = float('inf')
            if p[j] == '*':
                result = min(result, memo(i, j + 1))
                result = min(result, 1 + memo(i + 1, j))
            elif s[i] == p[j]:
                result = 1 + memo(i + 1, j + 1)

            cache[(i, j)] = result
            return result

        mini = float('inf')
        for start in range(len(s)):
            length = memo(start, 0)
            mini = min(mini, length)

        if memo(len(s), 0) == 0:
            mini = min(mini, 0)

        return -1 if mini == float('inf') else mini

## MLE
# TC: O(p + s*s*p)
# SC: O(s * p)
