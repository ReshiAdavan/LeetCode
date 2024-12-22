class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = i

            if t[i] not in tMap:
                tMap[t[i]] = i

            if sMap[s[i]] != tMap[t[i]]:
                return False

        return True

# TC: O(n)
# SC: O(n)
