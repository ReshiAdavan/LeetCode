from typing import List
from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        adjListRows, adjListCols = defaultdict(list), defaultdict(list)

        for above, below in rowConditions:
            adjListRows[above].append(below)
        for left, right in colConditions:
            adjListCols[left].append(right)

        rowOrdering = []
        visit, cycle = set(), set()

        def topSort(node, orderingList, table):
            if node in cycle:
                return False
            if node in visit:
                return True

            cycle.add(node)
            for nei in table[node]:
                if not topSort(nei, orderingList, table):
                    return False
            cycle.remove(node)
            visit.add(node)
            orderingList.append(node)
            return True

        for i in range(1, k + 1):
            if not topSort(i, rowOrdering, adjListRows):
                return []

        if not rowOrdering:
            return []

        visit, cycle = set(), set()
        colOrdering = []

        for i in range(1, k + 1):
            if not topSort(i, colOrdering, adjListCols):
                return []

        if not colOrdering:
            return []

        rowOrdering, colOrdering = rowOrdering[::-1], colOrdering[::-1]

        matrix = [[0] * k for _ in range(k)]
        rowMap = {num: i for i, num in enumerate(rowOrdering)}
        colMap = {num: i for i, num in enumerate(colOrdering)}

        for num in range(1, k + 1):
            matrix[rowMap[num]][colMap[num]] = num
        return matrix

# Size of rowConditions: R, Size of colConditions: C
# TC: O(R + C + k^2) 
# SC: O(R + C + k^2)
