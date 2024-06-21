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

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(cur, step, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return

            prev = -1
            for i in range(step, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(cur, i + 1, total + candidates[i])
                cur.pop()
                prev = candidates[i]

        dfs([], 0, 0)
        return res

# Beats 68.77% python submissions in runtime
# Beats 34.97% python submissions in memory usage
