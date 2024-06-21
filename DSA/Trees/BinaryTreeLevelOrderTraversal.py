# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: 
            return []
        if not root.right and not root.left: 
            return[[root.val]]
        ans = []
        q = collections.deque()
        if root: 
            q.append(root)
            
        while q: 
            val = []
            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            ans.append(val)     
        return ans

# Beats 69.84% python submissions in runtime
# Beats 66.47% python submissions in memory usage  