# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if self.isLeaf(root):
            return [root.val]

        return [root.val] + self.leftBoundary(root.left) + self.leaves(root) + self.rightBoundary(root.right)


    def leftBoundary(self, node):
        boundary = []
        while node:
            if not self.isLeaf(node):
                boundary.append(node.val)
            node = node.left if node.left else node.right
        return boundary

    def rightBoundary(self, node):
        boundary = []
        while node:
            if not self.isLeaf(node):
                boundary.append(node.val)
            node = node.right if node.right else node.left
        return boundary[::-1]

    def leaves(self, node):
        if not node:
            return []
        if self.isLeaf(node):
            return [node.val]
        return self.leaves(node.left) + self.leaves(node.right)

    def isLeaf(self, node):
        return not node.left and not node.right

# TC: O(n)
# SC: O(h) if balanced otherwise O(n)
