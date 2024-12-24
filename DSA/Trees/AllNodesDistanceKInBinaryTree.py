from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]

        graph = defaultdict(list)

        def trav(node, prev):
            if not node:
                return

            if prev:
                graph[node.val].append(prev.val)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)

            trav(node.left, node)
            trav(node.right, node)

        trav(root, None)

        res = []
        q = deque([[target.val, 0]])
        v = set([target.val])

        while q:
            nodeVal, dist = q.popleft()
            if dist == k:
                res.append(nodeVal)
            else:
                for nei in graph[nodeVal]:
                    if nei not in v:
                        v.add(nei)
                        q.append([nei, dist + 1])
        return res

# TC: O(n)
# SC: O(n)
