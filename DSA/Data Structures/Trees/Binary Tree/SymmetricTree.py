# Definition for a binary tree node.
from typing import Optional
from itertools import deque

## Recursive

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)

# TC: O(n)
# SC: O(n)

## Iterative (BFS) 

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([[root.left, root.right]])

        while q:
            node1, node2 = q.popleft()

            if not node1 and not node2:
                continue

            if (not node1 or not node2) or node1.val != node2.val:
                return False

            q.append([node1.left, node2.right])
            q.append([node1.right, node2.left])

        return True
    
# TC: O(n)
# SC: O(n)
