# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        def flat(node):
            if not node:
                return None

            leftTail = flat(node.left)
            rightTail = flat(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            end = rightTail or leftTail or node
            return end

        _ = flat(root)
        return root
    
# TC: O(n)
# SC: O(1) auxiliary
