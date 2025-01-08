from typing import List

# We also dont need a stack, can just pass string locally to each dfs / trav call
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(opens, closes, s):
            if opens == closes == n:
                res.append(s)

            if opens < n:
                dfs(opens + 1, closes, s + "(")

            if closes < opens:
                dfs(opens, closes + 1, s + ")")

        dfs(0, 0, '')
        return res
