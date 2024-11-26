from typing import List

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []
        for pos, dist in lights:
            events.append([pos - dist, 1])
            events.append([pos + dist + 1, -1])

        events.sort()

        maxBrightness = 0
        brightness = 0
        brightnessPos = float("inf")

        for pos, b in events:
            brightness += b
            if brightness > maxBrightness:
                maxBrightness = brightness
                brightnessPos = pos
        return brightnessPos


## Sweep-line algorithm
# TC: O(nlogn)
# SC: O(n)
