# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        sol = []
        q = collections.deque([root])

        while q:
            rs = None
            l = len(q)

            for i in range(l):
                node = q.popleft()
                if node:
                    rs = node
                    q.append(node.left)
                    q.append(node.right)
            if rs:
                sol.append(rs.val)
        return sol

# Beats 99.39% python submissions in runtime
# Beats 25.04% python submissions in memory usage  