# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def trav(node):
            if not node:
                return False

            left = trav(node.left)
            right = trav(node.right)
            parent = node == p or node == q

            if parent + right + left >= 2:
                self.ans = node

            return parent or left or right

        trav(root)
        return self.ans

# TC: O(n)
# SC: O(h)
