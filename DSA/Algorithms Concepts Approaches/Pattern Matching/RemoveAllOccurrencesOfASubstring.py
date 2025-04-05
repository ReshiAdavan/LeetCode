## KMP
class Solution:
    def lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def removeOccurrences(self, s: str, part: str) -> str:
        lps = self.lps(part)
        stack = []
        j = 0

        for char in s:
            stack.append(char)

            if stack[-1] == part[j]:
                j += 1
            else:
                # Instead of starting over, jump based on lps table
                while j > 0 and stack[-1] != part[j]:
                    j = lps[j - 1]
                if stack[-1] == part[j]:
                    j += 1

            if j == len(part):
                for _ in range(len(part)):
                    stack.pop()

                j = 0
                stackLen = len(stack)

                for i in range(max(0, stackLen - (len(part) - 1)), stackLen):
                    while j > 0 and stack[i] != part[j]:
                        j = lps[j - 1]

                    if stack[i] == part[j]:
                        j += 1

        return ''.join(stack)

## Let n rep. len(s) and m rep. len(part)
# TC: O(n + m); find pattern & replace pattern (constant compared to n)
# SC: O(n)

## Aho-Corasick
class ACNode:
    def __init__(self):
        self.children = {}
        self.failureLink = None
        self.end = False
        self.patternIndex = -1
        self.patternLength = 0

class AhoCorasick:
        # Build Aho-Corasick automaton
        # TC: O(m * k), m rep. len(pattern) and k rep. # of patterns -> O(m)
        def buildAutomaton(self, pattern):
            root = ACNode()

            # Build trie
            current = root
            for char in pattern:
                if char not in current.children:
                    current.children[char] = ACNode()
                current = current.children[char]

            current.end = True
            current.patternIndex = 0
            current.patternLength = len(pattern)

            # Build failure links
            queue = []
            for char, child in root.children.items():
                child.failureLink = root
                queue.append(child)

            while queue:
                current = queue.pop(0)

                for char, child in current.children.items():
                    queue.append(child)

                    failure = current.failureLink
                    while failure is not None and char not in failure.children:
                        failure = failure.failureLink

                    if failure is None:
                        child.failureLink = root
                    else:
                        child.failureLink = failure.children[char]
                        if child.failureLink.end:
                            child.end = True
                            child.patternIndex = child.failureLink.patternIndex
                            child.patternLength = child.failureLink.patternLength
            return root

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        aho = AhoCorasick()
        automaton = aho.buildAutomaton(part)
        result = []
        curState = automaton

        # TC: O(n + z); n rep. len(s), z rep. # of occurrences of part in s
        for char in s:
            result.append(char)

            while curState != automaton and char not in curState.children:
                curState = curState.failureLink

            if char in curState.children:
                curState = curState.children[char]

            if curState.end:
                patternLength = curState.patternLength
                for _ in range(patternLength):
                    result.pop()

                if result:
                    curState = automaton
                    for j in range(max(0, len(result) - len(part) + 1), len(result)):
                        c = result[j]
                        while curState != automaton and c not in curState.children:
                            curState = curState.failureLink

                        if c in curState.children:
                            curState = curState.children[c]
                else:
                    curState = automaton
        return ''.join(result)

# TC: O(n + m + z * m); process whole string, process each occurrence of part, remove thems
# SC: O(n + m); store string in stack and pattern in automaton
