# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float("-inf")
        
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
# Space Complexity: O(n)

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.max_path_sum = float("-inf")

        def trav(node):
            if not node:
                return 0

            left_path_sum = trav(node.left)
            right_path_sum = trav(node.right)
            cur_maxi = node.val
            if left_path_sum > 0:
                cur_maxi += left_path_sum
            if right_path_sum > 0:
                cur_maxi += right_path_sum

            self.max_path_sum = max(self.max_path_sum, cur_maxi)

            return max(node.val, node.val + max(left_path_sum, right_path_sum))

        trav(root)
        return self.max_path_sum

# Time Complexity: O(n)
# Space Complexity: O(h)