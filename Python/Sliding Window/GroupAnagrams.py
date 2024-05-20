class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return []
        res = []
        sCount, pCount = {}, {}
        l, r = 0, len(p) - 1

        for ch in p:
            if ch not in pCount: 
                pCount[ch] = 1
            else: 
                pCount[ch] += 1

        for i in range(l, r + 1):
            if s[i] not in sCount: 
                sCount[s[i]] = 1
            else: 
                sCount[s[i]] += 1

        while r < len(s):
            if sCount == pCount:
                res.append(l)

            if sCount[s[l]] > 1:
                sCount[s[l]] -= 1
            else:
                sCount.pop(s[l])
            l += 1

            r += 1
            if r < len(s):
                if s[r] not in sCount:
                    sCount[s[r]] = 1
                else:
                    sCount[s[r]] += 1
            else: 
                return res
            
# Beats 76.17 %of users with Python3
# Beats 99.01 %of users with Python3    