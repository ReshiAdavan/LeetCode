# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "NA"
            return f"{node.val},{preorder(node.left)},{preorder(node.right)}"

        return preorder(root)

    def deserialize(self, data):
        values = data.split(',')
        self.index = 0

        def dfs():
            if self.index >= len(values) or values[self.index] == "NA":
                self.index += 1
                return None

            node = TreeNode(int(values[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# TC: O(N)
# SC: O(N)
