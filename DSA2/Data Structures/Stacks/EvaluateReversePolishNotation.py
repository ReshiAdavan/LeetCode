from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                rightHand = stack.pop()
                leftHand = stack.pop()
                print(leftHand, rightHand)
                if token == "+":
                    stack.append(leftHand + rightHand)
                elif token == "-":
                    stack.append(leftHand - rightHand)
                elif token == "*":
                    stack.append(leftHand * rightHand)
                else:
                    if leftHand * rightHand < 0:
                        stack.append(abs(leftHand) // abs(rightHand) * -1)
                    else:
                        stack.append(abs(leftHand) // abs(rightHand))
        return stack[0]

# TC: O(n)
# SC: O(n)
