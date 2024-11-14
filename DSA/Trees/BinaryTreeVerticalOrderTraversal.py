# Definition for a binary tree node.
from typing import Optional, List
from itertools import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        columnTable = {}
        q = deque([[root, 0]])

        while q:
            node, index = q.popleft()
            if index not in columnTable:
                columnTable[index] = []
            columnTable[index].append(node.val)

            if node.left:
                q.append([node.left, index - 1])
            if node.right:
                q.append([node.right, index + 1])

        sortedColTable = dict(sorted(columnTable.items(), key=lambda item: item[0]))
        for v in sortedColTable.values():
            res.append(list(v))
        return res

# TC: O(n)
# SC: O(n)
