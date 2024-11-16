# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

class Solution(object):
    def maxDepth(self, root):
        if not root: 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Beats 92.59% python submissions in runtime
# Beats 73.85% python submissions in memory usage

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def trav(node):
            if not node:
                return 0
            return 1 + max(trav(node.left), trav(node.right))
        return trav(root)

# TC: O(n)
# SC: O(h)
