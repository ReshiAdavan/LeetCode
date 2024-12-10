from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            l, r = 0, len(matrix[0]) - 1
            if matrix[i][r] < target:
                i += 1
                continue
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            i += 1
        return False
        
# Beats 99.77% python submissions in runtime
# Beats 20.85% python submissions in memory usage  