class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        bktCount = 0

        for ch in s:
            if ch == "(":
                res.append(ch)
                bktCount += 1
            elif ch == ")":
                if bktCount > 0:
                    res.append(ch)
                    bktCount -= 1
            else:
                res.append(ch)

        if not bktCount:
            return "".join(res)

        for i in range(len(res) - 1, -1, -1):
            if res[i] == "(":
                res.pop(i)
                bktCount -= 1
            if not bktCount:
                return "".join(res)
        return ""

# TC: O(n)
# SC: O(n)
