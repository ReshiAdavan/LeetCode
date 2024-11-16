# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0
        self.diameter(root)
        return self.d
        
    def diameter(self, node):
        if not node:
            return 0
        left, right = self.diameter(node.left), self.diameter(node.right)
        self.d = max(self.d, left + right)
        return max(left, right) + 1

# Beats 67.65%  python submissions in runtime
# Beats 98.15% python submissions in memory usage

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def trav(node):
            if not node:
                return 0

            left_depth = trav(node.left)
            right_depth = trav(node.right)
            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        trav(root)
        return self.diameter

# TC: O(n)
# SC: O(h)
