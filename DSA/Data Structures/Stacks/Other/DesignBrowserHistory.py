class BrowserHistory:

    def __init__(self, homepage: str):
        self.prevHistory = []
        self.nextHistory = []
        self.curSite = homepage

    def visit(self, url: str) -> None:
        self.nextHistory = []
        self.prevHistory.append(self.curSite)
        self.curSite = url

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.prevHistory))
        for _ in range(steps):
            self.nextHistory.append(self.curSite)
            self.curSite = self.prevHistory.pop()
        return self.curSite


    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.nextHistory))
        for _ in range(steps):
            self.prevHistory.append(self.curSite)
            self.curSite = self.nextHistory.pop()
        return self.curSite

# TC: O(steps) 
# SC: O(n)
