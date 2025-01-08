class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = {}

    def _add(self, prevNode, freq):
        newNode = Node(freq)
        newNode.next = prevNode.next
        newNode.prev = prevNode
        newNode.next.prev = newNode
        prevNode.next = newNode
        return newNode

    def _remove(self, node):
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.table:
            currNode = self.table[key]
            currNode.keys.remove(key)

            nextFreq = currNode.freq + 1
            nextNode = currNode.next

            if nextNode == self.tail or nextNode.freq != nextFreq:
                nextNode = self._add(currNode, nextFreq)

            nextNode.keys.add(key)
            self.table[key] = nextNode
            self._remove(currNode)
        else:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq != 1:
                firstNode = self._add(self.head, 1)

            firstNode.keys.add(key)
            self.table[key] = firstNode

    def dec(self, key: str) -> None:
        currNode = self.table[key]
        currNode.keys.remove(key)

        if currNode.freq == 1:
            del self.table[key]
        else:
            prevFreq = currNode.freq - 1
            prevNode = currNode.prev

            if prevNode == self.head or prevNode.freq != prevFreq:
                prevNode = self._add(currNode.prev, prevFreq)

            prevNode.keys.add(key)
            self.table[key] = prevNode

        self._remove(currNode)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# TC: O(1)
# SC: O(n)
