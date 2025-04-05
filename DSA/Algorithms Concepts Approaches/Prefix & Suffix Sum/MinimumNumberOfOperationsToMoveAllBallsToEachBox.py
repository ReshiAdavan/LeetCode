from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answers = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i != j:
                    answers[i] += (abs(i - j) * int(boxes[j]))
        return answers

# TC: O(N^2)
# SC: O(1)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answers = []

        prefixCount, prefixPos = [0], [0]
        for i in range(len(boxes)):
            prefixCount.append(prefixCount[-1] + int(boxes[i]))
            prefixPos.append(prefixPos[-1] + (i * int(boxes[i])))

        suffixCount, suffixPos = [0], [0]
        for i in range(len(boxes) - 1, -1, -1):
            suffixCount.append(suffixCount[-1] + int(boxes[i]))
            suffixPos.append(suffixPos[-1] + (i * int(boxes[i])))

        suffixCount.reverse()
        suffixPos.reverse()

        for i in range(len(boxes)):
            leftCost = i * prefixCount[i] - prefixPos[i]
            rightCost = suffixPos[i + 1] - i * suffixCount[i + 1]
            answers.append(leftCost + rightCost)
        return answers

# TC: O(N)
# SC: O(N)
