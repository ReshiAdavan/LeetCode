from itertools import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        secrets = set([0, firstPerson])
        timesList = {}
        for x, y, t in meetings:
            if t not in timesList:
                timesList[t] = defaultdict(list)
            timesList[t][x].append(y)
            timesList[t][y].append(x)
        
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            secrets.add(node)
            for nei in timesList[t][node]:
                dfs(nei)


        for t in sorted(timesList.keys()):
            visit = set()
            for x in timesList[t]:
                if x in secrets:
                    dfs(x)
        return list(secrets)

# Time Complexity: O(mlog(m) + n)
# Space Complexity: O(max(n, m))
# Beats 72.64% of python users in runtime
# Beats 10.08% of python users in memory usage
