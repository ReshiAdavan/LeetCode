from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        sortedWords = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, _ in sortedWords[:k]]

# TC: O(n + nlogn + k) 
# SC: O(n)
