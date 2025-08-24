from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.terminal = False
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = TrieNode()
        self.contents = defaultdict(str)
    
    def search(self, path: str):
        if path == "/":
            return self.root
        parts = path.split("/")
        trav = self.root

        for part in parts[1:]:
            if part not in trav.children:
                return None
            trav = trav.children[part] 
        return trav

    def ls(self, path: str) -> List[str]:
        node = self.search(path)
        if node.terminal:
            return [path.split("/")[-1]]
        else:
            return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        parts = path.split("/")
        trav = self.root
        for part in parts[1:]:
            if part not in trav.children:
                trav.children[part] = TrieNode()
            trav = trav.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.search(filePath)
        if not node:
            self.mkdir(filePath)
            node = self.search(filePath)
        node.terminal = True
        self.contents[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.contents[filePath]

# TC: 
# SC: 
