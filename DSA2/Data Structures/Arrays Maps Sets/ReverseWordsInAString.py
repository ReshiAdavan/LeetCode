class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversedStrList = []

        for word in reversed(words):
            reversedStrList.append(word + " ")
        res = "".join(reversedStrList)
        return res[:len(res) - 1]

# TC: O(n)
# SC: O(n)
