from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowel(c: str) -> bool:
            return c in {'a', 'e', 'i', 'o', 'u'}

        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(n):
            word = words[i]
            is_valid = isVowel(word[0]) and isVowel(word[-1])
            prefix[i + 1] = prefix[i] + (1 if is_valid else 0)

        result = []
        for left, right in queries:
            count = prefix[right + 1] - prefix[left]
            result.append(count)
        return result

# TC: O(n + q)
# SC: O(n)
