from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def backtrack(left, right): 
            res = []
            for i in range(left, right + 1):
                symbol = expression[i]
                if symbol in ["+", "-", "*"]:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)

                    for n1 in nums1:
                        for n2 in nums2:
                            if symbol == "+":
                                res.append(n1 + n2)
                            elif symbol == "-":
                                res.append(n1 - n2)
                            else:
                                res.append(n1 * n2)
            if not res:
                res.append(int(expression[left: right + 1]))
            return res

        return backtrack(0, len(expression) - 1)

# TC: O(n * 2^n)
# SC: O(n * 2^n)
