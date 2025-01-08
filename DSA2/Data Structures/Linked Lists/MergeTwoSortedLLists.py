# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        sentinelNode = ListNode()
        SN_ptr = sentinelNode
        
        while list1 and list2: 
            if list1.val < list2.val: 
                SN_ptr.next = list1
                list1 = list1.next
                
            else: 
                SN_ptr.next = list2
                list2 = list2.next
            SN_ptr = SN_ptr.next
            
        if list1: 
                SN_ptr.next = list1
        elif list2: 
                SN_ptr.next = list2
        return sentinelNode.next

# Beats 89.34% python submissions in runtime
# Beats 59.21% python submissions in memory usage  