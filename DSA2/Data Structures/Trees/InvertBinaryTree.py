# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        if not root: 
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 

# Beats 81.47% python submissions in runtime
# Beats 49.33% python submissions in memory usage

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            trav(node.left)
            trav(node.right)

        trav(root)
        return root
    
# TC: O(n)
# SC:`O(h)
