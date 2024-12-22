class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversedStr = ""

        for word in reversed(words):
            reversedStr += (word + " ")

        return reversedStr[:len(reversedStr) - 1]

# TC: O(n)
# SC: O(n)
