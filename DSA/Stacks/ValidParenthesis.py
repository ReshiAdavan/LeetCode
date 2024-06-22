class Solution(object):
    def isValid(self, s):
        S, M, i = [], [], 0
        H = {'(': ")", '[': "]", '{': "}"}
        while i < len(s):
            if s[i] in H:
                S.append(s[i])
                M.append(H[s[i]])
            else:
                if len(M) == 0:
                    return False
                if s[i] != M[-1]:
                    return False
                else:
                    S.pop()
                    M.pop()
            i += 1
        if len(S) != 0 and len(M) != 0:
            return False
        return True

# Beats 91.81% python submissions in runtime
# Beats 12.49% python submissions in memory usage  