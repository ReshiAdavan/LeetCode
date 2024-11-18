# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p is root or q is root: 
            return root
        trav = root 
        while trav: 
            if p.val > trav.val and q.val > trav.val:
                trav = trav.right
            elif p.val < trav.val and q.val < trav.val:
                trav = trav.left
            else: 
                return trav
                
# Beats 81.08% python submissions in runtime
# Beats 51.82% python submissions in memory usage  

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def trav(node):
            if p.val > node.val and q.val > node.val:
                return trav(node.right)
            elif p.val < node.val and q.val < node.val:        
                return trav(node.left)
            else:
                return node
        return trav(root)

# Time Complexity: O(log(N))
# Space Complexity: O(h)