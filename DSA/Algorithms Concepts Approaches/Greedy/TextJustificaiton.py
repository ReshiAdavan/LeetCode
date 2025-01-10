from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        collection = []

        for word in words:
            if len(word) + len(collection) + sum(len(w) for w in collection) > maxWidth:
                output.append(collection)
                collection = []
            collection.append(word)
        if collection:
            output.append(collection)

        justified_lines = []
        for i, line in enumerate(output):
            if i == len(output) - 1 or len(line) == 1:
                justified_lines.append(" ".join(line).ljust(maxWidth))

            else:
                total_word_length = sum(len(word) for word in line)
                remaining_spaces = maxWidth - total_word_length
                min_space = remaining_spaces // (len(line) - 1)
                extra_space = remaining_spaces % (len(line) - 1)

                justified_line = ""
                for j in range(len(line) - 1):
                    justified_line += line[j] + " " * (min_space + (1 if j < extra_space else 0))
                justified_line += line[-1]
                justified_lines.append(justified_line)

        return justified_lines

## line-by-line gap-based algorithm
# TC: O(n)
# SC: O(n)
