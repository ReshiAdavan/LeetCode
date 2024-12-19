from collections import defaultdict
from math import random 

class RandomizedCollection:

    def __init__(self):
        self.table = defaultdict(set)
        self.data = []

    def insert(self, val: int) -> bool:
        self.table[val].add(len(self.data))
        self.data.append(val)
        return len(self.table[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.table or len(self.table[val]) == 0:
            return False
        lastVal = self.data[-1]
        index = self.table[val].pop()

        self.table[lastVal].add(index)
        self.data[index] = lastVal

        self.table[lastVal].discard(len(self.data) - 1)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# TC: O(1)
# SC: O(n)
