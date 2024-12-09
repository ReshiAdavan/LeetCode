from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnMap = {}
        q = deque([[root, 0, 0]])

        while q:
            for _ in range(len(q)):
                node, row, col = q.popleft()
                if col not in columnMap:
                    columnMap[col] = []
                columnMap[col].append([node.val, row])
                if node.left:
                    q.append([node.left, row + 1, col - 1])
                if node.right:
                    q.append([node.right, row + 1, col + 1])

        columnMap = dict(sorted(columnMap.items()))
        res = []

        for nodes in columnMap.values():
            nodes = sorted(nodes, key=lambda x: (x[1], x[0]))
            res.append([n for n, _ in nodes])
        return res
