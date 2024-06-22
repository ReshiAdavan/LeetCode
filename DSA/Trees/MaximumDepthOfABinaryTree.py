# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root: 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Beats 92.59% python submissions in runtime
# Beats 73.85% python submissions in memory usage  