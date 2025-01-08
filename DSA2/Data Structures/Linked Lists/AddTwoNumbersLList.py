from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        head = None
        ptr = None
        carry = 0
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            s %= 10
            if not head:
                head = ListNode(val=s, next=None)
                ptr = head
            else:
                ptr.next = ListNode(val=s, next=None)
                ptr = ptr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        if carry:
            ptr.next = ListNode(val=carry, next=None)
            ptr = ptr.next
        return head
