# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        if not root or not(root.left or root.right): 
            return True
       
        def height(root):
            if not root: 
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        if abs(height(root.left) - height(root.right)) > 1: 
            return False
        return True and self.isBalanced(root.left) and self.isBalanced(root.right)

# Beats 78.57% python submissions in runtime
# Beats 36.84% python submissions in memory usage

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def trav(node):
            if not node:
                return True

            if abs(self.depth(node.left) - self.depth(node.right)) > 1:
                return False
            return trav(node.left) and trav(node.right)

        return trav(root)

    def depth(self, node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))

# TC: O(n*n)
# SC: O(n)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def trav(node):
            if not node:
                return 0, True

            leftHeight, isLeftBalanced = trav(node.left)
            if not isLeftBalanced:
                return 0, False

            rightHeight, isRightBalanced = trav(node.right)
            if not isRightBalanced:
                return 0, False

            if abs(leftHeight - rightHeight) > 1:
                return 0, False
            return max(leftHeight, rightHeight) + 1, True

        _, isTreeBalanced = trav(root)
        return isTreeBalanced

# TC: O(n)
# SC: O(h)