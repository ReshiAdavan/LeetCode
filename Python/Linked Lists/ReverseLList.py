# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        p, c = None, head
        
        while c: 
            t = c.next
            c.next = p
            p = c
            c = t
        return p

# Beats 57.87% python submissions in runtime
# Beats 34.29% python submissions in memory usage  