from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        level = 0

        while q:
            prevNodeVal = None

            for _ in range(len(q)):
                node = q.popleft()

                if (level % 2 == 0 and (node.val % 2 == 0 or (prevNodeVal is not None and node.val <= prevNodeVal))):
                    return False
                if (level % 2 and (node.val % 2 or (prevNodeVal is not None and node.val >= prevNodeVal))):
                    return False

                prevNodeVal = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return True

# TC: O(n)
# SC: O(n)
