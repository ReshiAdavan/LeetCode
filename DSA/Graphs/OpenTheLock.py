class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def generatePatterns(s: str):
            res = []

            for i in range(4):
                # digit = digit + 1 (0 -> 1)
                digit = str((int(s[i]) + 1) % 10)
                res.append(s[:i] + digit + lock[i+1:])

                # digit = digit - 1 (9 -> 8)
                digit = str((int(s[i]) - 1 + 10) % 10)
                res.append(s[:i] + digit + lock[i+1:])
            return res

        q = deque()
        q.append(["0000", 0]) # [string, # of moves/turns]
        visited = set(deadends)

        while q:
            lock, turns = q.popleft()

            if lock == target: 
                return turns
            for pattern in generatePatterns(lock):
                if pattern not in visited:
                    visited.add(pattern)
                    q.append([pattern, turns + 1]) # [string, # of moves/turns]
        return -1
    
# Beats 57.76% python submissions in runtime
# Beats 92.19% python submissions in memory usage
