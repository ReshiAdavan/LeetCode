from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        lower = max(task[1] for task in tasks)
        upper = sum(task[0] for task in tasks) + lower

        def canComplete(energy):
            for actual, initial in tasks:
                if energy < initial:
                    return False
                energy -= actual
            return True

        res = upper
        while lower <= upper:
            curEnergy = (lower + upper) // 2
            if canComplete(curEnergy):
                upper = curEnergy - 1
                res = curEnergy
            else:
                lower = curEnergy + 1
        return res

# TC: O(nlogn + n + nlogn) = O(nlogn)
# SC: O(n) if we consider the space used to sort tasks list, else O(1)
