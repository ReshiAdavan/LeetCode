from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = deque(), deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            rIdx, dIdx = radiant.popleft(), dire.popleft()
            if rIdx < dIdx:
                radiant.append(rIdx + n)
            else:
                dire.append(dIdx + n)

        return "Radiant" if radiant else "Dire" 

# TC: O(N)
# SC: O(N)
