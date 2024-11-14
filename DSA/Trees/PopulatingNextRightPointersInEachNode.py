# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

## BFS

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(1, len(q)):
                q[i - 1].next = q[i]
        return root

# TC: O(n)
# SC: O(n)

## Recursive DFS

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        def trav(node):
            if not node:
                return
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            trav(node.left)
            trav(node.right)

        trav(root)
        return root

# TC: O(n)
# SC: O(1) / Recurisve O(n) technically

## BFS

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        cur, ahead = root, root.left if root else None
        while cur and ahead:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = ahead
                ahead = cur.left
        return root

# TC: O(n)
# SC: O(1)