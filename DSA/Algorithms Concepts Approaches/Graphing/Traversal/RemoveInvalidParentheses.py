from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # bfs
        visited = {s}
        queue = [s]
        found = False
        result = []

        while queue and not found:
            nextLevel = []

            for expr in queue:
                if self.isValid(expr):
                    result.append(expr)
                    found = True

                if found:
                    continue

                # removals
                for i in range(len(expr)):
                    if expr[i] in "()":
                        if i > 0 and expr[i] == expr[i - 1]:
                            continue
                        newExpr = expr[:i] + expr[i + 1:]
                        if newExpr not in visited:
                            visited.add(newExpr)
                            nextLevel.append(newExpr)
            queue = nextLevel
        return result if result else [""]

    def isValid(self, s: str) -> int:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

# TC: O(N * 2^N)
# SC: O(N * 2^N)
