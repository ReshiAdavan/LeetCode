from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        r, c = 0, m - 1

        while r < n and c >= 0:
            val = matrix[r][c]

            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1

        return False

# TC: O(n + m)
# SC: O(1)
