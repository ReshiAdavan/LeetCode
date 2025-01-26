# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def trav(node):
            if not node:
                return None
            if node.val > key:
                node.left = trav(node.left)
            elif node.val < key:
                node.right = trav(node.right)

            else:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right

                curr = node.right
                while curr.left:
                    curr = curr.left
                successor = curr.val

                node.val = successor
                node.right = self.deleteNode(node.right, successor)

            return node
        return trav(root)

# TC: O(logn) ~ O(H)
# SC: O(N)
