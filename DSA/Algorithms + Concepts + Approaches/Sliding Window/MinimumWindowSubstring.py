class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        fT, fW = {}, {}
        for c in t:
            fT[c] = 1 + fT.get(c, 0)

        have, need = 0, len(fT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            fW[c] = 1 + fW.get(c, 0)
            if c in fT and fW[c] == fT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                fW[s[l]] -= 1
                if s[l] in fT and fT[s[l]] > fW[s[l]]:
                    have -= 1
                l += 1

        left, right = res
        return s[left: right + 1] if resLen != float("inf") else ""

# Time Complexity: O(s + t)
# Space Complexity: O(s + t)