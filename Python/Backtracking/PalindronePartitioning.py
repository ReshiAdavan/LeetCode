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
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(step):
            if step >= len(s): 
                res.append(cur.copy())
                return
            
            for i in range(step, len((s))):
                if self.isPalindrome(s[step:i + 1]):
                    cur.append(s[step:i + 1])
                    dfs(i + 1)
                    cur.pop()

        dfs(0)
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

# Beats 95.71% python submissions in runtime
# Beats 41.03% python submissions in memory usage 