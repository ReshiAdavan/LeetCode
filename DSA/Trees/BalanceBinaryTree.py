# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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