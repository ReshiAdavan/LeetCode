# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        ptr = head
        while ptr:
            if ptr.child:
                child_tail = self.mergeChild(ptr.child)

                # child's tail to ptr.next
                if ptr.next:
                    child_tail.next = ptr.next
                    ptr.next.prev = child_tail

                # ptr to its child, child to None
                ptr.next = ptr.child
                ptr.child.prev = ptr
                ptr.child = None

            ptr = ptr.next
        return head

    def mergeChild(self, node):
        ptr = node
        while ptr.next:
            if ptr.child:
                child_tail = self.mergeChild(ptr.child)

                # child's tail to ptr.next
                if ptr.next:
                    child_tail.next = ptr.next
                    ptr.next.prev = child_tail

                # ptr to its child, child to None
                ptr.next = ptr.child
                ptr.child.prev = ptr
                ptr.child = None

            ptr = ptr.next
        return ptr

# TC: O(n)
# SC: O(1)
