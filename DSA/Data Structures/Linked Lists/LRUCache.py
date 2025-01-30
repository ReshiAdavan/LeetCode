from collections import OrderedDict

# OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        return None

# Time Complexity: O(1)
# Space Complexity: O(capacity)
# Beats 100.00% of python users in runtime
# Beats 95.65% of python users in memory usage

# Doubly LL + hashmap

class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node 
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._add(n)
            n.value = value
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

# Time Complexity: O(1)
# Space Complexity: O(capacity)
# Beats 100.00% of python users in runtime
# Beats 92.77% of python users in memory usage
