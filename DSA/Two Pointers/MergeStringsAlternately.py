class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = []

        while p1 < len(word1) or p2 < len(word2):
            c1 = word1[p1] if p1 < len(word1) else " "
            c2 = word2[p2] if p2 < len(word2) else " "

            if c1 != " ":
                res.append(c1)

            if c2 != " ":
                res.append(c2)

            p1, p2 = p1 + 1, p2 + 1

        return "".join(res)

# TC: O(n + m)
# SC: O(n + m)
