# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return None

            node.left = trav(node.left)
            node.right = trav(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return trav(root)

# TC: O(N)
# SC: O(H)
