class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        for ch in s:
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for ch, f in stack:
            res += f * ch
        return res

# TC: O(n)
# SC: O(n)
