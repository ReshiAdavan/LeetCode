from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(i, prev, cur, expr):
            if i == len(num):
                if cur == target:
                    res.append(expr)
                return

            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break
                curNum = int(num[i: j + 1])

                if i == 0:
                    backtrack(j + 1, curNum, curNum, str(curNum))
                else:
                    backtrack(j + 1, curNum, cur + curNum, expr + "+" + str(curNum))
                    backtrack(j + 1, -curNum, cur - curNum, expr + "-" + str(curNum))
                    backtrack(j + 1, prev * curNum, 
                             cur - prev + (prev * curNum), 
                             expr + "*" + str(curNum))

        backtrack(0, 0, 0, "")
        return res

# TC: O(4^n)
# SC: O(n)
