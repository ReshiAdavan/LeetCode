from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            c = Counter(word)
            c[word[i]] -= 1
            if not c[word[i]]:
                del c[word[i]]
            if len(set(c.values())) == 1:
                return True
        return False
    
# TC: O(n^2)
# SC: O(n)

class Solution(object):
    def equalFrequency(self, word):
        counter = Counter(word)

        for ch in word:
            counter[ch] -= 1

            if counter[ch] == 0:
                del counter[ch]

            if len(set(counter.values())) == 1:
                return True

            counter[ch] += 1
        return False

# TC: O(n)
# SC: O(n)
