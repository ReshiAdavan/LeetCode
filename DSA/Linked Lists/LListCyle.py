# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
class Solution(object):
    def hasCycle(self, head):
        if not head: 
            return False
        H = {}
        while head:
            if head in H: 
                return True
            H[head] = ListNode(head.val)
            head = head.next
        return False
    
# Beats 36.54% python submissions in runtime
# Beats 22.08% python submissions in memory usage  

# Solution 2 (Tortoise and Hare algorihm)
class Solution(object):
    def hasCycle(self, head):
        if not head: 
            return False
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False

# Beats 75.05% python submissions in runtime
# Beats 83.07% python submissions in memory usage  