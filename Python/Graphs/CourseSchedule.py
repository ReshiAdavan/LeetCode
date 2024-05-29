class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        AList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            AList[crs].append(pre)

        v = set()
        def DFS(crs):
            if crs in v: 
                return False
            if AList[crs] == []: 
                return True

            v.add(crs)
            for pre in AList[crs]:
                if not DFS(pre): 
                    return False
            v.remove(crs)
            AList[crs] = []
            return True

        for c in range(numCourses):
            if not DFS(c): 
                return False
        return True

# Beats 71.79% python submissions in runtime
# Beats 29.72% python submissions in memory usage 