from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        leftMins = [-1] * n
        rightMins = [n] * n

        stack1 = []
        for i in range(n):
            while stack1 and arr[stack1[-1]] >= arr[i]:
                stack1.pop()
            if stack1:
                leftMins[i] = stack1[-1]
            stack1.append(i)

        stack2 = []
        for i in range(n - 1, -1, -1):
            while stack2 and arr[stack2[-1]] > arr[i]:
                stack2.pop()
            if stack2:
                rightMins[i] = stack2[-1]
            stack2.append(i)

        res = 0
        for i in range(n):
            res += arr[i] * (i - leftMins[i]) * (rightMins[i] - i)
            res %= mod
        return res

# TC: O(N)
# SC: O(N)
