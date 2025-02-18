from typing import List

class Node:
    def __init__(self):
        self.words = []  # access leaf node words per node
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]

            # Add words
            curr.words.append(word)

        # Sort at end
        curr.words.sort()

    def returnTopWords(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        # return top three
        return curr.words[:3]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        wordSearch = Trie()
        for product in sorted(products):
            wordSearch.addWord(product)

        results = []
        for i in range(len(searchWord)):
            results.append(wordSearch.returnTopWords(searchWord[:i + 1]))

        return results

# N rep. len(searchWord), M rep. len(products), L rep. avg. len(products)
# TC: O(MlogM + L + N)
# SC: O(N * L)
