class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def memo(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                cache[(i, j)] = memo(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(
                    memo(i, j + 1),  # Insert
                    memo(i + 1, j + 1),  # Replace
                    memo(i + 1, j)  # Delete
                )
            return cache[(i, j)]

        return memo(0, 0)

# TC: O(n * m)
# SC: O(n * m)
