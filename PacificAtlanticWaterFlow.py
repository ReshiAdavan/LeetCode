class Solution(object):
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        PO, AO = set(), set()

        def dfs(r, c, visited, h):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or heights[r][c] < h:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, PO, heights[0][c])
            dfs(rows - 1, c, AO, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, PO, heights[r][0])
            dfs(r, cols - 1, AO, heights[r][cols - 1])

        resultList = list(PO.intersection(AO))
        return resultList

# Beats 96.15% python submissions in runtime
# Beats 54.07% python submissions in memory usage