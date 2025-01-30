class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i >= len(word):
                return node.end

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)

        return dfs(self.root, 0)

# L represents length of word
# N represents number of words
# K represents alphabet/character set size

# TC: O(L) for addWord, O(K^L) for search
# SC: O(N * L)
