# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def DFS(root, maxi):
            if not root:
                return 
            curr = root.val
            if(curr >= maxi):
                self.result += 1
                maxi = curr
            DFS(root.left, maxi)
            DFS(root.right, maxi)
        
        
        self.result = 0
        DFS(root, root.val)
        return self.result

# Beats 64.45% python submissions in runtime
# Beats 45.48% python submissions in memory usage

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def trav(node, maxi):
            if not node:
                return 0

            if node.val < maxi:
                return (trav(node.left, max(maxi, node.val)) + 
                    trav(node.right, max(maxi, node.val)))

            return (1 + 
                trav(node.left, max(maxi, node.val)) + 
                trav(node.right, max(maxi, node.val)))

        return trav(root, float(-inf))
    
# Beats 39.63% of users in runtime
# Beats 94.51% of users in memory
# Time Complexity: O(N)
# Space Complexity: O(1)