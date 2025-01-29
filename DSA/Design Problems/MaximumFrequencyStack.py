class FreqStack:
    def __init__(self):
        self.counter = {}  # frequency counter per elem
        self.table = {}  # (k, v) -> (freq, stack)
        self.maxFreq = 1

    def push(self, val: int) -> None:
        # increment frequency of value
        if val not in self.counter:
            self.counter[val] = 0
        self.counter[val] += 1
        freq = self.counter[val]

        # add value to group of most frequent elements
        if freq not in self.table:
            self.table[freq] = []
        self.table[freq].append(val)

        # set new maximuum frequency if there is one
        self.maxFreq = max(self.maxFreq, self.counter[val])

    def pop(self) -> int:
        # get most frequent element from group of most frequent elements
        res = self.table[self.maxFreq].pop()

        # decrement frequency of that value specifically
        self.counter[res] -= 1

        # if the most frequent group is empty, decrement maxFreq to the next most frequent group
        if not self.table[self.maxFreq]:
            self.maxFreq -= 1

        return res

# TC: O(1)
# SC: O(n)
