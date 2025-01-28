# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def trav(node):
            if not node:
                # [robbed children, didnt rob children]
                return [0, 0]

            left, right = trav(node.left), trav(node.right)

            robCur = node.val + left[1] + right[1]
            notRobCur = max(left) + max(right)

            return [robCur, notRobCur]

        return max(trav(root))

# TC: O(N)
# SC: O(H)
