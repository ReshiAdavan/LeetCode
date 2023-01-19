class Solution(object):
    def hasAllCodes(self, s, k):
        codeSet = set()
        self.subString(s, k, codeSet)
        return len(codeSet) == 2 ** k

    def subString(self, s, k, codeSet):
        left, right = 0, k - 1

        while right < len(s):
            if s[left:right + 1] not in codeSet:
                codeSet.add(s[left:right + 1])

            left += 1
            right += 1

# Beats 70.45% python submissions in runtime
# Beats 70.45% python submissions in memory usage