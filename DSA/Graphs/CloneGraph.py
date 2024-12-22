# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        M = {}

        def dfs(node):
            if node in M:
                return M[node]
            
            copy = Node(node.val)
            M[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else None

# Beats 78.72% python submissions in runtime
# Beats 83.69% python submissions in memory usage  