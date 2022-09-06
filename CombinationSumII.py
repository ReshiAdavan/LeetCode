class Solution(object):
    def combinationSum2(self, candidates, target):
        combinationList = []
        candidates.sort()

        def DFS(i, cur, total):
            if total == target:
                combinationList.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            DFS(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            DFS(i + 1, cur, total)

        DFS(0, [], 0)
        return combinationList 

# Beats 49.70% python submissions in runtime
# Beats 81.63% python submissions in memory usage