class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2 + str1 != str1 + str2: return ""
        if len(str1) == len(str2): return str1
        if len(str1) > len(str2): 
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

# Beats 100.00% in runtime (0ms)
# Beats 23.07% in memory 