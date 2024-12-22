class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        def evalSubExpr(op, subExpr):
            if op == "&":
                operands = subExpr.split(",")
                res = "t"
                for operand in operands:
                    if operand == "f":
                        return "f"
                return res
            elif op == "|":
                operands = subExpr.split(",")
                res = "f"
                for operand in operands:
                    if operand == "t":
                        return "t"
                return res
            else:
                return "f" if subExpr == "t" else "t"

        for ch in expression:
            if ch == ")":
                subExpr = ""
                while stack[-1] != "(":
                    subExpr = stack.pop() + subExpr

                stack.pop()
                op = stack.pop()

                stack.append(evalSubExpr(op, subExpr))
            else:
                stack.append(ch)

        return stack[-1] == "t"

# TC: O(n)
# SC: O(n)
