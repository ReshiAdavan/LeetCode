class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        prevSpan = 0

        while self.stack and self.stack[-1][0] <= price:
            _, prevSpan = self.stack.pop()
            span += prevSpan

        self.stack.append([price, span])
        return span


# TC: O(n)
# SC: O(n)
