# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float(-inf)
        
        def maxGain(node):
            if not node:
                return 0
            
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            currentPathSum = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, currentPathSum)
            return node.val + max(leftGain, rightGain)
        
        maxGain(root)
        return self.maxSum

# Beats 80.98% of users in runtime 
# Beats 97.54% of users in memory
# Time Complexity: O(n)
# Space Complexity: O(1)
