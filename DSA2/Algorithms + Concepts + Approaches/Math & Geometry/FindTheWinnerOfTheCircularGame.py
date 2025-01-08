## Iterative

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n + 1)]
        index = 0

        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)
        return friends[0]

# TC: O(n^2)
# SC: O(n)

## Recursive

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def josephus(n, k):
            if n == 1:
                return 0
            return (josephus(n - 1, k) + k) % n
        return josephus(n, k) + 1

# TC: O(n)
# SC: O(n)
