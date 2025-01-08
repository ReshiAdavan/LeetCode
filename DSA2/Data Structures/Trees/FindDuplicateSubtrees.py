from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        table = defaultdict(int)
        res = []

        def serialize(node):
            if not node:
                return "NA"

            s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            table[s] += 1

            if table[s] == 2:
                res.append(node)

            return s

        serialize(root)
        return res

# TC: O(N)
# SC: O(N)
