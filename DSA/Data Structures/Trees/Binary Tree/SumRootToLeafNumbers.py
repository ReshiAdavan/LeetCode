# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 10 + node.val

            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)

# TC: O(N)
# SC: O(H)
