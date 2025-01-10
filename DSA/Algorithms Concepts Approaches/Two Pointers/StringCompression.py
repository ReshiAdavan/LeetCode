from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        writeIndex = 0

        while left < len(chars):
            right = left + 1
            while right < len(chars) and chars[left] == chars[right]:
                right += 1

            chars[writeIndex] = chars[left]
            writeIndex += 1

            if right - left > 1:
                for digit in str(right - left):
                    chars[writeIndex] = digit
                    writeIndex += 1

            left = right
        return writeIndex

# TC: O(n)
# SC: O(1)
