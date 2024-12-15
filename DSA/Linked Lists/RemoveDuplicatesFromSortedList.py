# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr = head.next
        prev = head

        while ptr:
            if ptr.val == prev.val:
                # remove ptr node
                temp = ptr.next
                prev.next = temp
                ptr = ptr.next
            else:
                prev = ptr
                ptr = ptr.next
        return head

# TC: O(n)
# SC: O(1)
