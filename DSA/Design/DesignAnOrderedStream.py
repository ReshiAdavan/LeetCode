from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey - 1] = value

        chunk = []
        while self.pointer < len(self.list) and self.list[self.pointer] is not None:
            chunk.append(self.list[self.pointer])
            self.pointer += 1
        return chunk

# TC: O(n)
# SC: O(n)
