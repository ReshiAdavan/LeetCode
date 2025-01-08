from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = Counter(s)
        freqMap = dict(sorted(freqMap.items(), key=lambda x: x[1], reverse=True))

        res = ""
        for frequency, char in freqMap.items():
            res += (frequency * char)

        return res

## Hashmap + Heap/Sort
# TC: O(n * log(n))
# SC: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        res = ""

        for char, freq in freqMap.items():
            buckets[freq].append(char)

        for freq in reversed(range(len(buckets))):
            for char in buckets[freq]:
                res += (freq * char)
        return res

## Hashmap + 2D Array
# TC: O(n)
# SC: O(n)