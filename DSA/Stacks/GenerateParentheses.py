from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def trav(opens, closes, stack):
            if opens == n and closes == n:
                res.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                trav(opens + 1, closes, stack)
                stack.pop()

            if closes < opens:
                stack.append(")")
                trav(opens, closes + 1, stack)
                stack.pop()

        trav(0, 0, [])
        return res

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
