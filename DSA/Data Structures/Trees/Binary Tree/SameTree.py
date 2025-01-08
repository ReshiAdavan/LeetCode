# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q: 
            return True
        if not p or not q:
            return False
        if p and q and p.val != q.val: 
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
# Beats 90.60% python submissions in runtime
# Beats 38.27% python submissions in memory usage

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def trav(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return trav(n1.left, n2.left) and trav(n1.right, n2.right)
        return trav(p, q)

# TC: O(n)
# SC: O(h)