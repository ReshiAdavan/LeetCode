# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sentinelNode, carry = ListNode(), 0
        tmp = sentinelNode
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            tmp.next = ListNode(val)

            tmp = tmp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sentinelNode.next

# Beats 61.44% python submissions in runtime
# Beats 6.29% python submissions in memory usage                