class Solution(object):
    def combinationSum(self, candidates, target):
        combinationList = []

        def DFS(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                combinationList.append(cur[:])
                return

            cur.append(candidates[i])
            DFS(i, cur, total + candidates[i])
            cur.pop()
            DFS(i + 1, cur, total)

        DFS(0, [], 0)
        return combinationList

# Beats 73.46% python submissions in runtime
# Beats 23.20% python submissions in memory usage