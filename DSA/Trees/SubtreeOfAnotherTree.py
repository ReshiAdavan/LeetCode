# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot): 
        if not root:
            return False
        if self.isSameTree(root, subRoot): 
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, subRoot): 
        if not root and not subRoot: 
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False

# Beats 86.95% python submissions in runtime
# Beats 56.48% python submissions in memory usage

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def trav(mainTreeNode, subTreeNode):
            if not mainTreeNode and not subTreeNode:
                return True
            if not mainTreeNode or not subTreeNode:
                return False
            return (
                mainTreeNode.val == subTreeNode.val
                and trav(mainTreeNode.left, subTreeNode.left) 
                and trav(mainTreeNode.right, subTreeNode.right)
            )

        if trav(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# TC: O(m*n)
# SC: O(h)