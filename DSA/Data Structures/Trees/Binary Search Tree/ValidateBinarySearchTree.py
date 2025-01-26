from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))

# Beats 68.06% python submissions in runtime
# Beats 66.94% python submissions in memory usage  

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def trav(node, mini, maxi):
            if not node:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return trav(node.left, mini, node.val) and trav(node.right, node.val, maxi)
        return trav(root, float("-inf"), float("inf"))