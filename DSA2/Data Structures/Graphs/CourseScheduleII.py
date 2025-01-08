from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visit, cycle = set(), set()
        ordering = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            ordering.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return ordering
    
# Time Complexity: O(P + N)
# Space Complexity: O(P + N)
# Beats 70.62% of python users in runtime
# Beats 15.96% of python users in memory usage
