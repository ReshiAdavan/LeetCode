# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        s = []
        trav = root
        while s or trav: 
            while trav: 
                s.append(trav)
                trav = trav.left
            trav = s.pop()
            k -= 1 
            if k == 0:
                return trav.val
            trav = trav.right

# Beats 87.31% python submissions in runtime
# Beats 83.73% python submissions in memory usage
# Time Complexity: O(k) 
# Space Complexity: O(k)