from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                top = self.prefixMatrix[r][c + 1]
                self.prefixMatrix[r + 1][c + 1] = prefix + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefixMatrix[row2 + 1][col2 + 1]
        top = self.prefixMatrix[row1][col2 + 1]
        left = self.prefixMatrix[row2 + 1][col1]
        topLeft = self.prefixMatrix[row1][col1]
        return bottomRight - top - left + topLeft

# TC: O(1) / O(N * M) pre-compute
# SC: O((M + 1) * (N + 1))
