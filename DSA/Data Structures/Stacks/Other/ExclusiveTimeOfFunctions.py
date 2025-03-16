from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        exclusiveTimes = [0] * n

        for log in logs:
            id, status, time = log.split(":")
            if stack and stack[-1][0] == id and stack[-1][1] == "start" and status == "end":
                _, _, endTime = stack.pop()
                exclusiveTimes[int(id)] += (int(time) - int(endTime) + 1)
                if stack:
                    stack[-1][2] = int(time) + 1
            else:
                if stack:
                    prevId, _, prevTime = stack[-1]
                    exclusiveTimes[int(prevId)] += (int(time) - int(prevTime))
                stack.append([id, status, time])
        return exclusiveTimes

# N rep. # of functions, L rep. # of logs
# TC: O(L)
# SC: O(N + L)
