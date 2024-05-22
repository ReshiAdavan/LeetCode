"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        curr = root
        dummy = Node(-1)
        head = root

        while head:
            curr = head
            prev = dummy
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next
            dummy.next = None
        return root
    
# Beats 89.04% of users with Python3 in runtime
# Beats 64.13% of users with Python3 in memory