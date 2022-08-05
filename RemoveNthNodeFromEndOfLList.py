# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        trav = head
        length = 1
        while trav.next: 
            length += 1
            trav = trav.next
        k, i = length - (n - 1), 1
        if i == k: 
            return head.next
        trav, previous = head, None
        while i < k: 
            if i == k - 1: 
                previous = trav
            trav = trav.next
            i += 1 
        previous.next, trav.next = trav.next, None
        return head

# Beats 97.38% python submissions in runtime
# Beats 68.18% python submissions in memory usage  