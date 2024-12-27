from typing import List
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adj[pattern].append(word)

        parents = defaultdict(set)
        q = deque([(beginWord, 0)])
        seen = {beginWord: 0}
        minDist = float('inf')

        while q:
            word, dist = q.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for nei in adj[pattern]:
                    if nei not in seen or seen[nei] == dist + 1 <= minDist:
                        if nei == endWord:
                            minDist = dist + 1
                        parents[nei].add(word)

                        if nei not in seen:
                            seen[nei] = dist + 1
                            q.append((nei, dist + 1))
        del adj, seen

        answers = []

        def makeSequences(word, seq):
            if word == beginWord:
                answers.append(seq[::-1])
            else:
                for parent in parents[word]:
                    makeSequences(parent, seq + [parent])

        makeSequences(endWord, [endWord])
        return answers

# TC: O(n * m)
# SC: O(n * m)
