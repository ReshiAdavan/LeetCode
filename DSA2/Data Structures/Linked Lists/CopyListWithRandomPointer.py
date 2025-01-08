"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        ListOfNodes, temp = {None: None}, head
        while temp:
            ListOfNodes[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:  
            n = ListOfNodes[temp]
            n.next = ListOfNodes[temp.next]
            n.random = ListOfNodes[temp.random]
            temp = temp.next
        return ListOfNodes[head]

# Beats 87.54% python submissions in runtime
# Beats 42.28% python submissions in memory usage  