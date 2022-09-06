class Solution(object):
    def partition(self, s):
        resultList, partition = [], []
        length = len(s)

        def DFS(i):
            if i >= length:
                resultList.append(partition[:])
                return
            for j in range(i, length):
                if self.isPalindrone(s, i, j):
                    partition.append(s[i : j + 1])
                    DFS(j + 1)
                    partition.pop()

        DFS(0)
        return resultList

    def isPalindrone(self, s, i, j):
        if len(s) <= 1:
            return True
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# Beats 90.96% python submissions in runtime
# Beats 35.79% python submissions in memory usage 