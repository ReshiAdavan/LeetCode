class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        i, j = 0, 0

        while i < n1 and j < n2:
            steps = ord(str1[i]) - ord(str2[j])
            if steps == 0 or steps == -1 or (str1[i] == 'z' and str2[j] == 'a'):
                i += 1
                j += 1
            else:
                i += 1

        return j == n2

# TC: O(n + m)
# SC: O(1)
